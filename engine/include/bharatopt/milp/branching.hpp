#pragma once
#include "bharatopt/model/model.hpp"
#include "bharatopt/lp/lp_solver.hpp"

namespace bharatopt {

class BranchingStrategy {
public:
    // Selects the index of the variable to branch on, and outputs its fractional value.
    // Returns -1 if no fractional variable is found (i.e. solution is integer).
    static int most_fractional(const Model& model, const LPSolution& sol, double& out_frac_val);
};

} // namespace bharatopt
