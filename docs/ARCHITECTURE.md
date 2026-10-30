# Architecture Overview

```text
                         BHARATOPT-X
                            │
              Sovereign Optimization Engine
                            │
                    Industrial User
                            │
                  Web Studio / API Layer
                            │
                 Data Ingestion & Parsing
                            │
                  Automatic Classifier
                            │
         ┌────────────┬─────┴──────┬────────────┐
         │            │            │            │
         LP          MILP          QP          NLP
         │            │            │            │
    ┌────┴────┐       │       ┌────┴────┐  ┌────┴────┐
    │         │   PRESOLVE    │         │  │         │
 Primal     Dual      │     Convex Nonconvex Convex Nonconvex
 Simplex  Simplex LP RELAXATION │   │      │         │
    │         │       │         IPM Active ADMM   Future:
    └────┬────┘   ┌───┴───┐         Set          Spatial B&B
         │        │       │
    Strategy  Heuristics Cuts
    Selector      │       │
         │    Stronger Bound
         │        │
         │    BRANCHING
         │        │
         │   SEARCH TREE
         │        │
         └────────┼─────────────────┘
                  │
        Sparse Math Engine (SpMV / Cholesky)
                  │
        ┌─────────┴─────────┐
        │                   │
   CPU Manager        GPU Manager
   (OpenMP/SIMD)    (CUDA/cuSPARSE)
        │                   │
        └─────────┬─────────┘
                  │
        Verified Optimization
                  │
        ┌─────────┴─────────┐
        │                   │
 Certificates          Diagnostics
 (KKT / MIP Gap)       (Shadow Prices)
                  │
         Decision Support Layer
         (BharatOpt Sahayak)
                  │
           Business Insights
```

## Directory Structure
- `engine/`: Core C++23 optimization algorithms (LP, MILP, QP, NLP, LA).
- `apps/`: Standalone executables and CLI tools.
- `services/`: API and microservices for the web interface and tuning.
- `web/`: React frontend for business users.
- `ml/`: GNN branching, parameter tuning, and instance analysis models.
- `tests/`: GoogleTest suite.
- `benchmarks/`: Performance and regression benchmarks.
- `docs/`: Architecture and roadmap documents.
- `data/`: Sample optimization instances and datasets.
- `scripts/`: Build, CI/CD, and utility scripts.
