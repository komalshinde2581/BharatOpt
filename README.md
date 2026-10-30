# BharatOpt-X
**Indigenous GPU-Accelerated Optimization Solver (Sovereign Alternative)**

BharatOpt-X is a production-grade, mathematically robust, and GPU-accelerated optimization engine built entirely from scratch in C++23. It serves as a sovereign alternative to commercial solvers like IBM CPLEX, Gurobi, and FICO Xpress for India's strategic industrial sectors (refining, logistics, manufacturing).

## Features
- **Core Solvers**: Two-Phase Simplex, Primal-Dual IPM, Active Set, Branch-and-Bound, Branch-and-Cut.
- **Problem Types**: LP, MILP, Convex QP, NLP, MIQP Router.
- **Sparse Linear Algebra**: Native CSR/CSC matrix tracking and transformations.
- **Next-Gen ML Integration**: PyTorch Graph Neural Network (GNN) branching via an external bipartite graph sidecar.
- **Certification & Robustness**: Mathematically certified optimality proofs (Primal/Dual certificates).
- **Sovereign Engine**: 100% written in modern C++. Zero reliance on legacy open-source solvers (CBC, GLPK, HiGHS).

## Project Structure
- `engine/`: Core C++23 Mathematical solvers (LP, MILP, Sparse, Routing, NLP).
- `ml/` & `services/`: PyTorch Geometric ML sidecar and Flask API.
- `web/`: HTML/JS/D3.js interactive dashboard for Business and Engineer views.
- `data/`: Sample `.mps` optimization model files for testing.
- `tests/`: Extensive GoogleTest validation suite covering all phases.
- `docs/`: In-depth architecture reports, benchmarks, and capability documentation.

## How to Run (SIH Submission Demo)
The project includes an automated demo script that sets up the correct Visual Studio MSVC environment, builds the engine, executes the main binary on a sample MPS model, and runs the 28-suite test verification.

**From PowerShell:**
```powershell
.\run_sih_demo.ps1
```

### Starting the Machine Learning GNN Branching Service
BharatOpt-X offloads complex MILP branching decisions to a PyTorch Geometric sidecar.
```bash
# Install dependencies
pip install -r requirements.txt
# Start the GNN inference API
python services/gnn/inference_service.py
```

### Viewing the User Interface
Open `web/index.html` in any modern web browser to view the Business Dashboard and the interactive Simplex/Branch-and-Bound visualizer.
