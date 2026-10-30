add_library(engine_lib 
    src/engine.cpp
    lp/lp_solver.cpp
    presolve/presolve.cpp
    milp/branch_and_bound.cpp
    milp/branching.cpp
)
target_include_directories(engine_lib PUBLIC include)
