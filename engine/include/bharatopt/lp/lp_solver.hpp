#pragma once
#include "bharatopt/model/model.hpp"
#include <vector>
#include <map>

namespace bharatopt {

struct LPSolution {
    double objective = 0.0;
    std::vector<double> primal_values;
    bool is_feasible = false;
    bool is_optimal = false;
};

class TreeLPSolver {
public:
    // Solves the LP relaxation of the model, respecting the temporary local_bounds
    // applied at the current Branch & Bound node.
    LPSolution solve(const Model& model, const std::map<int, Bounds>& local_bounds);
};

} // namespace bharatopt
