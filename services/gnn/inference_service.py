import json
import torch
from flask import Flask, request, jsonify
import sys
import os

# Add ml/gnn to path to import model
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../ml/gnn')))
try:
    from model import BipartiteGNN
except ImportError:
    BipartiteGNN = None

app = Flask(__name__)

# Initialize model (mock weights for now)
if BipartiteGNN:
    gnn_model = BipartiteGNN(var_features_dim=5, cons_features_dim=3, hidden_dim=64)
    gnn_model.eval()
else:
    gnn_model = None

@app.route('/predict_branching', methods=['POST'])
def predict_branching():
    """
    Endpoint called by BharatOpt-X C++ Engine during MILP Branch & Bound.
    Receives bipartite graph features and returns the best variable index to branch on.
    """
    try:
        data = request.json
        # Expected structure: {"var_features": [...], "cons_features": [...], "edges": [[...], [...]]}
        
        if not gnn_model:
            return jsonify({"error": "GNN Model not loaded."}), 500

        # Convert to tensors
        x_var = torch.tensor(data.get('var_features', []), dtype=torch.float32)
        x_cons = torch.tensor(data.get('cons_features', []), dtype=torch.float32)
        edge_index = torch.tensor(data.get('edges', []), dtype=torch.long)
        
        # Inference
        with torch.no_grad():
            scores = gnn_model(x_var, x_cons, edge_index)
            
        # Select variable with highest score
        best_var_index = torch.argmax(scores).item()
        
        return jsonify({
            "status": "success",
            "branching_variable": best_var_index,
            "confidence_score": scores[best_var_index].item()
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    print("Starting BharatOpt-X GNN Inference Service on port 5050...")
    app.run(host='0.0.0.0', port=5050)
