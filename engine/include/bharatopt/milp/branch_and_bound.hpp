#pragma once
#include "bharatopt/model/model.hpp"
#include "bharatopt/lp/lp_solver.hpp"
#include <vector>
#include <map>
#include <memory>
#include <limits>
#include <queue>

namespace bharatopt {

struct Node {
    int id;
    int depth;
    std::map<int, Bounds> local_bounds;
    LPSolution relaxation;

    // For Best-Bound First search
    bool operator<(const Node& other) const {
        return relaxation.objective < other.relaxation.objective; // Maximize
    }
};

struct MILPSolution {
    double objective = -std::numeric_limits<double>::infinity();
    std::vector<double> primal_values;
    bool is_feasible = false;
    bool is_optimal = false;
    double best_bound = std::numeric_limits<double>::infinity();
    int nodes_explored = 0;
};

class BranchAndBound {
public:
    BranchAndBound(const Model& model);
    
    MILPSolution solve();

private:
    const Model& model_;
    TreeLPSolver lp_solver_;
    double incumbent_obj_;
    std::vector<double> incumbent_vals_;
    int node_count_;
    
    // Process a single node. Returns false if pruned.
    bool process_node(const Node& node, std::priority_queue<Node>& queue);
    bool is_integer_feasible(const LPSolution& sol, int& fractional_var, double& fractional_val);
};

} // namespace bharatopt
