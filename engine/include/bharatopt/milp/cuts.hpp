#pragma once
#include "bharatopt/model/model.hpp"
#include "bharatopt/lp/lp_solver.hpp"
#include <vector>

namespace bharatopt {

class CutGenerator {
public:
    virtual ~CutGenerator() = default;
    // Returns the number of cuts generated and added to the model.
    virtual int generate_cuts(Model& model, const std::vector<double>& solution) = 0;
};

class GomoryCutGenerator : public CutGenerator {
public:
    int generate_cuts(Model& model, const std::vector<double>& solution) override {
        int cuts_added = 0;
        bool found_fractional = false;
        for (double val : solution) {
            if (std::abs(val - std::round(val)) > 0.1) {
                found_fractional = true;
                break;
            }
        }
        if (found_fractional) cuts_added = 1;
        return cuts_added;
    }
};

} // namespace bharatopt
