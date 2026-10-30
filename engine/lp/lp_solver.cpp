#include "bharatopt/lp/lp_solver.hpp"
#include <iostream>

namespace bharatopt {

LPSolution TreeLPSolver::solve(const Model& model, const std::map<int, Bounds>& local_bounds) {
    LPSolution sol;
    sol.is_feasible = true;
    sol.is_optimal = true;
    sol.objective = 0.0;
    
    // Resize primal values based on variables
    int num_vars = model.variables().size();
    sol.primal_values.resize(num_vars, 0.0);

    // MOCK IMPLEMENTATION:
    // We will assign values based on bounds. If a variable is bounded strictly, we use its bound.
    // Otherwise, we assign a fractional value to force branching in our test scenarios.
    
    for (int i = 0; i < num_vars; ++i) {
        double lower = 0.0;
        double upper = 100.0; // Default mock upper
        
        // Apply global bounds
        if (model.get_variable(i)) {
            lower = model.get_variable(i)->bounds().lower;
            upper = model.get_variable(i)->bounds().upper;
        }

        // Apply local bounds from the B&B node
        if (local_bounds.find(i) != local_bounds.end()) {
            lower = std::max(lower, local_bounds.at(i).lower);
            upper = std::min(upper, local_bounds.at(i).upper);
        }

        if (lower > upper) {
            sol.is_feasible = false;
            sol.is_optimal = false;
            return sol;
        }

        // Mock assignment:
        // If lower == upper, the variable is fixed (integer usually in B&B)
        if (lower == upper) {
            sol.primal_values[i] = lower;
        } else {
            // Assign a fractional value midway to trigger branching, unless it naturally lands on an int.
            sol.primal_values[i] = lower + 0.5;
            if (sol.primal_values[i] > upper) {
                sol.primal_values[i] = upper;
            }
        }
        
        // Mock objective calculation: maximize sum of vars
        sol.objective += sol.primal_values[i] * 10.0;
    }

    return sol;
}

} // namespace bharatopt
