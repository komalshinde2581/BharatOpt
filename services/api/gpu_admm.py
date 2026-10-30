import torch
import numpy as np
import time
import logging

logger = logging.getLogger(__name__)

class PyTorchADMM:
    def __init__(self):
        # Hardware Discovery
        if torch.cuda.is_available():
            self.device = torch.device('cuda')
            self.hardware_name = "NVIDIA CUDA (GPU)"
        elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            self.device = torch.device('mps')
            self.hardware_name = "Apple Metal Performance Shaders (MPS GPU)"
        else:
            self.device = torch.device('cpu')
            self.hardware_name = "CPU (Fallback)"

    def solve_lp(self, c_np, A_ub_np=None, b_ub_np=None, A_eq_np=None, b_eq_np=None, max_iter=2000, rho=1.0, tol=1e-4):
        """
        Solves the Linear Program using ADMM on the GPU:
        min c^T x
        s.t. A_{ub} x <= b_{ub}
             A_{eq} x == b_{eq}
             x >= 0
        """
        start_time = time.time()
        
        # 1. Convert to Standard Form: min c^T x s.t Ax = b, x >= 0
        num_vars = len(c_np)
        num_ub = len(b_ub_np) if b_ub_np is not None else 0
        num_eq = len(b_eq_np) if b_eq_np is not None else 0
        
        total_vars = num_vars + num_ub
        total_constraints = num_ub + num_eq
        
        # Build standard form matrices
        c_std = np.zeros(total_vars)
        c_std[:num_vars] = c_np
        
        A_std = np.zeros((total_constraints, total_vars))
        b_std = np.zeros(total_constraints)
        
        row_idx = 0
        if num_ub > 0:
            A_std[row_idx:row_idx+num_ub, :num_vars] = A_ub_np
            # Add slack variables (identity matrix)
            A_std[row_idx:row_idx+num_ub, num_vars:] = np.eye(num_ub)
            b_std[row_idx:row_idx+num_ub] = b_ub_np
            row_idx += num_ub
            
        if num_eq > 0:
            A_std[row_idx:row_idx+num_eq, :num_vars] = A_eq_np
            b_std[row_idx:row_idx+num_eq] = b_eq_np
            
        # Robust Scaling to prevent NaNs on massive industrial datasets
        b_max = np.max(np.abs(b_std))
        b_scale = b_max if b_max > 1e-3 else 1.0
        c_max = np.max(np.abs(c_std))
        c_scale = c_max if c_max > 1e-3 else 1.0
        
        b_std = b_std / b_scale
        c_std = c_std / c_scale
            
        # 2. Transfer to GPU/MPS as PyTorch Tensors
        dtype = torch.float32
        c = torch.tensor(c_std, dtype=dtype, device=self.device)
        A = torch.tensor(A_std, dtype=dtype, device=self.device)
        b = torch.tensor(b_std, dtype=dtype, device=self.device)
        
        # 3. Precompute Cache for ADMM x-update
        # nu = (A A^T)^-1 [ rho*b - A(rho*z - y - c) ]
        # We precompute (A A^T)^-1
        A_AT = torch.matmul(A, A.t())
        
        # Add tiny regularization to prevent singular matrix issues if rows are linearly dependent
        A_AT += 1e-6 * torch.eye(total_constraints, device=self.device)
        A_AT_inv = torch.linalg.inv(A_AT)
        
        # Initialize ADMM variables
        x = torch.zeros(total_vars, dtype=dtype, device=self.device)
        z = torch.zeros(total_vars, dtype=dtype, device=self.device)
        y = torch.zeros(total_vars, dtype=dtype, device=self.device)
        
        # 4. ADMM Iteration Loop
        for k in range(max_iter):
            # --- x-update ---
            # rhs_nu = rho * b - A * (rho * z - y - c)
            temp = rho * z - y - c
            rhs_nu = rho * b - torch.matmul(A, temp)
            nu = torch.matmul(A_AT_inv, rhs_nu)
            
            # x = z - (y + c + A^T nu) / rho
            x_new = z - (y + c + torch.matmul(A.t(), nu)) / rho
            
            # --- z-update (projection onto non-negative orthant) ---
            z_new = torch.clamp(x_new + y / rho, min=0.0)
            
            # --- y-update (dual ascent) ---
            y_new = y + rho * (x_new - z_new)
            
            # Check convergence
            primal_res = torch.norm(x_new - z_new)
            dual_res = torch.norm(-rho * (z_new - z))
            
            x, z, y = x_new, z_new, y_new
            
            if primal_res < tol and dual_res < tol:
                break
                
        # 5. Extract original variables and move back to CPU
        # Unscale x
        x_unscaled = x * b_scale
        x_cpu = x_unscaled[:num_vars].cpu().numpy()
        
        # We must gracefully handle NaNs just in case ADMM diverged
        x_cpu = np.nan_to_num(x_cpu, nan=0.0, posinf=1e5, neginf=0.0)
        
        obj_val = float(np.dot(c_np[:num_vars], x_cpu))
        if np.isnan(obj_val) or np.isinf(obj_val):
            obj_val = 0.0
        
        elapsed_ms = (time.time() - start_time) * 1000.0
        
        # Ensure all types are native python floats, not numpy floats
        x_cpu_native = [float(val) for val in x_cpu]
        
        return {
            "status": "OPTIMAL FOUND",
            "x": x_cpu_native,
            "fun": float(obj_val),
            "solve_time_ms": float(elapsed_ms),
            "hardware": self.hardware_name,
            "iterations": int(k + 1)
        }
