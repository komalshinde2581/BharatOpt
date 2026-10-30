#include "bharatopt/milp/branch_and_bound.hpp"
#include <iostream>
#include <cmath>

namespace bharatopt {

BranchAndBound::BranchAndBound(const Model& model) 
    : model_(model), incumbent_obj_(-std::numeric_limits<double>::infinity()), node_count_(0) {}

MILPSolution BranchAndBound::solve() {
    std::cout << "[B&B] Starting Branch and Bound tree search...\n";
    
    std::priority_queue<Node> queue;
    
    // Root Node
    Node root;
    root.id = ++node_count_;
    root.depth = 0;
    root.relaxation = lp_solver_.solve(model_, root.local_bounds);
    
    if (!root.relaxation.is_feasible) {
        std::cout << "[B&B] Root node is infeasible.\n";
        return MILPSolution{};
    }
    
    queue.push(root);
    
    while (!queue.empty()) {
        Node current = queue.top();
        queue.pop();
        
        process_node(current, queue);
    }
    
    MILPSolution final_sol;
    if (incumbent_obj_ != -std::numeric_limits<double>::infinity()) {
        final_sol.is_feasible = true;
        final_sol.is_optimal = true;
        final_sol.objective = incumbent_obj_;
        final_sol.primal_values = incumbent_vals_;
    }
    final_sol.nodes_explored = node_count_;
    // Best bound is the incumbent object if optimal, else could be tracked via queue.
    final_sol.best_bound = incumbent_obj_; 
    
    std::cout << "[B&B] Search complete. Nodes Explored: " << node_count_ << "\n";
    return final_sol;
}

bool BranchAndBound::process_node(const Node& node, std::priority_queue<Node>& queue) {
    // 1. Prune by bound
    if (node.relaxation.objective <= incumbent_obj_) {
        // std::cout << "      Node " << node.id << " pruned by bound.\n";
        return false;
    }
    
    int frac_var = -1;
    double frac_val = 0.0;
    
    // 2. Prune by integrality / New Incumbent
    if (is_integer_feasible(node.relaxation, frac_var, frac_val)) {
        incumbent_obj_ = node.relaxation.objective;
        incumbent_vals_ = node.relaxation.primal_values;
        std::cout << "[B&B] * New Integer Incumbent found at Node " << node.id 
                  << " | Obj: " << incumbent_obj_ << "\n";
        return false;
    }
    
    // 3. Branch
    // Left Child: x <= floor(val)
    Node left_child;
    left_child.id = ++node_count_;
    left_child.depth = node.depth + 1;
    left_child.local_bounds = node.local_bounds;
    left_child.local_bounds[frac_var].upper = std::floor(frac_val);
    if (left_child.local_bounds[frac_var].lower > left_child.local_bounds[frac_var].upper) {
        // Infeasible bound
    } else {
        left_child.relaxation = lp_solver_.solve(model_, left_child.local_bounds);
        if (left_child.relaxation.is_feasible && left_child.relaxation.objective > incumbent_obj_) {
            queue.push(left_child);
        }
    }
    
    // Right Child: x >= ceil(val)
    Node right_child;
    right_child.id = ++node_count_;
    right_child.depth = node.depth + 1;
    right_child.local_bounds = node.local_bounds;
    right_child.local_bounds[frac_var].lower = std::ceil(frac_val);
    if (right_child.local_bounds[frac_var].lower > right_child.local_bounds[frac_var].upper) {
        // Infeasible bound
    } else {
        right_child.relaxation = lp_solver_.solve(model_, right_child.local_bounds);
        if (right_child.relaxation.is_feasible && right_child.relaxation.objective > incumbent_obj_) {
            queue.push(right_child);
        }
    }
    
    return true;
}

bool BranchAndBound::is_integer_feasible(const LPSolution& sol, int& fractional_var, double& fractional_val) {
    for (size_t i = 0; i < sol.primal_values.size(); ++i) {
        const Variable* var = model_.get_variable(i);
        if (var && (var->type() == VariableType::Integer || var->type() == VariableType::Binary)) {
            double val = sol.primal_values[i];
            if (std::abs(val - std::round(val)) > 1e-5) {
                fractional_var = i;
                fractional_val = val;
                return false;
            }
        }
    }
    return true;
}

} // namespace bharatopt
