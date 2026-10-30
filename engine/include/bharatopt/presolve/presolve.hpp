#pragma once
#include "bharatopt/model/model.hpp"

namespace bharatopt {

class Presolver {
public:
    // Tightens bounds and removes redundant constraints before solving
    static void run(Model& model);
};

} // namespace bharatopt
