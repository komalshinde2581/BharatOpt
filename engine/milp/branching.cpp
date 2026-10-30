#include "bharatopt/milp/branching.hpp"
#include <cmath>

namespace bharatopt {

int BranchingStrategy::most_fractional(const Model& model, const LPSolution& sol, double& out_frac_val) {
    int best_var = -1;
    double max_fractionality = 0.0;
    
    for (size_t i = 0; i < sol.primal_values.size(); ++i) {
        const Variable* var = model.get_variable(i);
        if (var && (var->type() == VariableType::Integer || var->type() == VariableType::Binary)) {
            double val = sol.primal_values[i];
            double fractionality = std::abs(val - std::round(val));
            
            // Check if it is noticeably fractional
            if (fractionality > 1e-5) {
                // Distance to nearest 0.5 (where fractionality is exactly 0.5)
                double dist_to_half = 0.5 - std::abs(0.5 - fractionality);
                
                if (dist_to_half > max_fractionality) {
                    max_fractionality = dist_to_half;
                    best_var = i;
                    out_frac_val = val;
                }
            }
        }
    }
    
    return best_var;
}

} // namespace bharatopt
