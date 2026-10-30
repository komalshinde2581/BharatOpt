import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, ListStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem

def generate_report():
    filename = "BharatOpt_Case_Study_Expert_Review.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#0f172a"),
        alignment=1, # Center
        spaceAfter=25
    )

    h1_style = ParagraphStyle(
        'Heading1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#1e40af"),
        spaceBefore=18,
        spaceAfter=10
    )

    h2_style = ParagraphStyle(
        'Heading2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        textColor=colors.HexColor("#334155"),
        spaceBefore=12,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=16,
        textColor=colors.HexColor("#334155"),
        spaceAfter=10
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=16,
        textColor=colors.HexColor("#334155")
    )

    content = []
    
    # Title
    content.append(Paragraph("BharatOpt-X: Sovereign Optimization Architecture", title_style))
    content.append(Paragraph("A Comprehensive Technical Case Study for Expert Review", ParagraphStyle('Sub', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=14, alignment=1, spaceAfter=30)))

    # Executive Summary
    content.append(Paragraph("1. Executive Summary & Objective", h1_style))
    content.append(Paragraph("The BharatOpt-X platform was engineered with a strict mandate: <b>Sovereign optimization core with no dependency on commercial optimization engines</b>. Unlike commercial or open-source wrappers that rely on external libraries (e.g., Gurobi, CPLEX, or Xpress), BharatOpt-X utilizes a clean-room indigenous mathematical engine. Designed specifically for the rigorous demands of industrial operations like the MRPL (Mangalore Refinery), the system provides certified optimal solutions, exact dual sensitivity (shadow pricing), and hardware-accelerated matrix operations.", body_style))

    # Architecture & Workflow
    content.append(Paragraph("2. Deep-Dive Workflow Architecture", h1_style))
    content.append(Paragraph("The system implements a strictly decoupled frontend-backend architecture to ensure high-performance execution without blocking the UI.", body_style))
    
    content.append(Paragraph("A. Data Ingestion & Transformation", h2_style))
    content.append(Paragraph("Users submit algebraic constraints via a Natural Language formulation or directly via a structured JSON schema. The Python FastAPI backend validates the inputs using Pydantic, normalizes inequality directions, and transpiles the payload into an industry-standard MPS (Mathematical Programming System) flat file. This ensures compatibility and provides a standardized buffer between the web API and the core solver.", body_style))

    content.append(Paragraph("B. Engine Dispatch & Execution", h2_style))
    content.append(Paragraph("The backend delegates the computation to the `native_simplex.py` engine or the C++23 native core (`bharatopt_engine.exe`). The solver strictly avoids third-party optimization black-boxes, performing its own matrix factorizations and pivot operations.", body_style))

    content.append(Paragraph("C. Post-Optimization Diagnostics", h2_style))
    content.append(Paragraph("Upon termination, the engine computes not just the primal decision variables, but the exact KKT residuals. It returns primal slacks/surpluses, dual variables (shadow prices), and reduced costs. The API enriches this mathematical output with contextual economic advice.", body_style))

    # Solver Roles
    content.append(Paragraph("3. Mathematical Optimization Engines (Solver Roles)", h1_style))
    content.append(Paragraph("The sovereign core is divided into four distinct algorithmic pathways, routed automatically based on model characteristics:", body_style))
    
    solvers = [
        "<b>Linear Programming (LP) Engine:</b> Implements a highly stabilized Two-Phase Revised Simplex algorithm. Phase I minimizes a sum of artificial variables to rigorously establish a Basic Feasible Solution (BFS) or definitively prove infeasibility. Phase II optimizes the primary objective function.",
        "<b>Mixed-Integer Linear Programming (MILP) Engine:</b> Extends the LP core using a Branch & Cut framework. It is designed to handle discrete decision variables (boolean, integer) required for lot-sizing and complex scheduling.",
        "<b>Quadratic Programming (QP) Engine:</b> Utilizes a Primal-Dual Interior Point Method (IPM) to optimize convex quadratic objectives subject to linear constraints. Critical for financial risk models like the Markowitz portfolio.",
        "<b>Non-Linear Programming (ADMM) Engine:</b> Employs the Alternating Direction Method of Multipliers. This allows decentralized consensus coupling across large-scale multi-unit refineries, breaking down massive non-linear interactions into solvable sub-problems."
    ]
    items = [ListItem(Paragraph(text, bullet_style)) for text in solvers]
    content.append(ListFlowable(items, bulletType='bullet', spaceAfter=15))

    # Technology Stack
    content.append(Paragraph("4. Technology Stack & Performance Characteristics", h1_style))
    stack = [
        "<b>API Layer (Python/FastAPI):</b> Chosen for asynchronous I/O, guaranteeing that long-running algorithmic solves do not block concurrent UI requests.",
        "<b>Computational Core (C++23 & Python/NumPy):</b> Hand-written pivoting algorithms ensure complete codebase sovereignty. Linear algebra subroutines use optimized vectorization.",
        "<b>Hardware Acceleration (CUDA/OpenMP):</b> The solver engine dynamically probes for NVIDIA hardware. If present, sparse matrix multiplications and Cholesky updates stream through <b>cuSPARSE/cuBLAS</b>. Otherwise, it safely falls back to CPU multi-core OpenMP.",
        "<b>Frontend (Vanilla JS/TailwindCSS):</b> A highly responsive 'Studio' interface utilizing Chart.js for real-time optimal basis visualization."
    ]
    content.append(ListFlowable([ListItem(Paragraph(text, bullet_style)) for text in stack], bulletType='bullet', spaceAfter=15))

    # UI & Decision Support
    content.append(Paragraph("5. User Interface & Decision Support (UI Elements)", h1_style))
    content.append(Paragraph("The UI transcends traditional numerical output by providing actionable intelligence:", body_style))
    ui_elements = [
        "<b>Sovereign Solve Badge & Benchmarks:</b> An active telemetry overlay verifies the hardware being used (CUDA vs. CPU) and tracks the exact millisecond latency and VRAM footprint.",
        "<b>Optimality Certification:</b> Provides KKT-based optimality verification for applicable continuous convex models; MILP optimality is certified through bounds and zero MIP gap.",
        "<b>Decision Support Layer (BharatOpt Sahayak):</b> The flagship decision-support panel. It intercepts the exact dual variables and automatically maps them into business strategy (e.g., 'Shadow price is $4.50. Expand bottleneck capacity only if marginal cost is below this threshold')."
    ]
    content.append(ListFlowable([ListItem(Paragraph(text, bullet_style)) for text in ui_elements], bulletType='bullet', spaceAfter=15))

    # Failure Handling
    content.append(Paragraph("6. Robustness & Failure State Handling", h1_style))
    content.append(Paragraph("Industrial applications demand safe, explanatory failures rather than cryptic stack traces. The system was strictly tested against edge cases:", body_style))
    failure_states = [
        "<b>Infeasibility Detection:</b> If Phase I terminates with a non-zero artificial objective, the UI clearly flags the conflict (e.g., demand outstripping maximum capacity limits).",
        "<b>Unbounded Ray Identification:</b> If a pivot column exhibits a negative reduced cost but no positive pivot row elements, the solver aborts, mathematically proving unboundedness, and the UI instructs the user to check for missing resource caps.",
        "<b>Malformed Schema Resilience:</b> Invalid JSON or syntax errors in the mathematical formulation are trapped at the Pydantic API layer, rendering a clean 400 Bad Request error directly in the UI console without crashing the engine."
    ]
    content.append(ListFlowable([ListItem(Paragraph(text, bullet_style)) for text in failure_states], bulletType='bullet', spaceAfter=15))

    # Conclusion
    content.append(Paragraph("Conclusion", h1_style))
    content.append(Paragraph("The BharatOpt-X prototype establishes a highly viable architectural pattern for industrial mathematical optimization. By completely eliminating reliance on external black-box solvers, integrating real-time shadow pricing logic into the UI, and proving optimality through KKT residuals and MIP gaps, it meets the rigorous criteria required by expert panels and sovereign industrial applications.", body_style))

    doc.build(content)
    print(f"Report generated: {os.path.abspath(filename)}")

if __name__ == '__main__':
    generate_report()
