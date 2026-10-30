import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """Canvas that computes total pages dynamically for clean 'Page X of Y' footers."""
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return  # Skip cover page
            
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header
        self.drawString(54, 750, "BharatOpt-X | Prototype Reference Handbook & Glossary")
        self.drawRightString(558, 750, "MRPL / Smart India Hackathon (SIH)")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 744, 558, 744)
        
        # Footer
        self.line(54, 45, 558, 45)
        self.drawString(54, 32, "Sovereign Optimization Core Platform")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 32, page_text)
        self.restoreState()

def build_pdf(filename="BharatOpt_X_Prototype_Handbook_and_Glossary.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    primary_color = colors.HexColor("#1E3A8A")   # Indigo / Navy
    secondary_color = colors.HexColor("#0D6EFD") # Blue
    accent_color = colors.HexColor("#7C3AED")    # Purple
    dark_text = colors.HexColor("#1E293B")
    muted_text = colors.HexColor("#475569")
    bg_light = colors.HexColor("#F8FAFC")

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=primary_color,
        alignment=0,
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=13,
        leading=18,
        textColor=secondary_color,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=primary_color,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=secondary_color,
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=dark_text,
        spaceAfter=6
    )

    body_bold = ParagraphStyle(
        'Body_Bold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#334155")
    )

    term_title = ParagraphStyle(
        'TermTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=accent_color
    )

    term_def = ParagraphStyle(
        'TermDef',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=dark_text
    )

    story = []

    # -------------------------------------------------------------
    # COVER / TITLE SECTION
    # -------------------------------------------------------------
    story.append(Spacer(1, 20))
    story.append(Paragraph("BHARATOPT-X OPTIMIZATION STUDIO", title_style))
    story.append(Paragraph("Complete Technical Handbook, Screen Guide & Mathematical Glossary", subtitle_style))
    
    meta_table = [
        [Paragraph("<b>Target Enterprise:</b>", body_style), Paragraph("Mangalore Refinery and Petrochemicals Limited (MRPL)", body_style)],
        [Paragraph("<b>Programme:</b>", body_style), Paragraph("Smart India Hackathon (SIH) — Sovereign R&D Initiative", body_style)],
        [Paragraph("<b>Architecture:</b>", body_style), Paragraph("100% Clean-Room Native C++23 Engine (Zero External Commercial Solvers)", body_style)],
        [Paragraph("<b>Document Version:</b>", body_style), Paragraph("2.4 (Prototype Final Review Edition)", body_style)],
        [Paragraph("<b>Date:</b>", body_style), Paragraph("September 2026", body_style)],
    ]
    t = Table(meta_table, colWidths=[130, 370])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('PADDING', (0,0), (-1,-1), 6),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t)
    story.append(Spacer(1, 15))

    # Executive Overview Callout
    overview_text = (
        "<b>Executive Purpose:</b> This document is designed as an all-in-one comprehensive field guide for the "
        "BharatOpt-X Optimization Studio. It explains every visual screen widget, button, menu item, diagnostic "
        "panel, and mathematical solver term in simple, intuitive language. Whether presenting before the SIH jury "
        "or technical leadership at MRPL, this handbook provides the exact terminology and conceptual foundations "
        "needed to defend the platform with complete confidence."
    )
    story.append(Table([[Paragraph(overview_text, callout_style)]], colWidths=[500], style=[
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#BFDBFE")),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(Spacer(1, 15))

    # -------------------------------------------------------------
    # SECTION 1: VISUAL PROTOTYPE SCREEN-BY-SCREEN GUIDE
    # -------------------------------------------------------------
    story.append(Paragraph("1. Comprehensive Visual Prototype Screen Guide", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=secondary_color, spaceAfter=8))
    story.append(Paragraph(
        "The BharatOpt-X Web Studio is modeled after modern industrial engineering IDEs (Integrated Development Environments) "
        "such as Visual Studio Code and JetBrains, providing refinery engineers with an intuitive, unified workspace.", body_style
    ))

    screen_features = [
        ("Top Menu Bar", "Contains standard application dropdowns (File, Edit, Solver, Hardware, View, Help). File allows blank model creation, local file loading (.json, .mps, .mod), sample loading, and full export. Solver allows selecting specific native algorithms or custom KKT tolerances."),
        ("Hardware Badge (Top-Right)", "A pulsing green indicator reading <i>'NVIDIA CUDA: NVIDIA GeForce RTX 3050 Laptop GPU (4 GB VRAM) [ACTIVE]'</i>. Confirms that GPU-accelerated cuSPARSE and cuBLAS sparse linear algebra kernels are live and initialized."),
        ("Ribbon Toolbar", "Hosts one-click execution controls: The blue <b>Solve Model</b> play button, <b>New Model</b> reset, <b>BharatOpt Sahayak (AI)</b> shortcut, the <b>Algorithm Selector</b>, the <b>Hardware Backend Selector</b> (GPU vs. CPU OpenMP), and the <b>Presolve</b> toggle."),
        ("Optimization Suite (Left Tree)", "File browser listing all 4 pre-loaded industrial benchmark models (01_lp_crude_blending, 02_milp_electronics, 03_qp_portfolio_risk, 04_admm_refinery). Clicking any model instantly loads its code, updates stats, and prepares it for solving."),
        ("Problem Browser (Left Bottom)", "Dynamic real-time model profiler showing total variables (n), total constraints (m), objective sense (MAX/MIN), total Non-Zero coefficients (NNZ), matrix density (%), and mathematical polytope validity."),
        ("Dual Code Editor (Center)", "Tabbed editor allowing instant switching between structured JSON API format (<code>model.json</code>) and human-readable structured English (<code>algebraic_model.mod</code>). Includes a JSON prettifier and live character counters."),
        ("Console & Analytics Panel (Bottom)", "Multi-tab diagnostic center with 5 specialized workspaces: (1) Engine Log & Output, (2) Visual Analytics & Charts, (3) Branch & Bound Tree Visualizer, (4) Simplex Pivot Inspector, and (5) Hardware Profiler (GPU)."),
        ("BharatOpt Sahayak (AI Panel)", "Real-time AI decision intelligence dashboard on the bottom-right. Formulates the certified optimal objective value, variable allocation list, active bottleneck constraints, and strategic business advice. Includes a 1-click Copy button and interactive What-If query box.")
    ]

    for title, desc in screen_features:
        story.append(Paragraph(f"• <b>{title}:</b> {desc}", body_style))

    story.append(Spacer(1, 10))

    # -------------------------------------------------------------
    # SECTION 2: THE 5 CONSOLE TABS EXPLAINED
    # -------------------------------------------------------------
    story.append(Paragraph("2. Deep Dive: The 5 Diagnostic Workspaces", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=secondary_color, spaceAfter=8))

    tab_data = [
        [
            Paragraph("<b>Tab Name</b>", body_bold),
            Paragraph("<b>What It Shows on Screen</b>", body_bold),
            Paragraph("<b>Engineering Significance (Why it Matters)</b>", body_bold)
        ],
        [
            Paragraph("<b>1. Engine Log & Output</b>", body_style),
            Paragraph("Live streaming terminal output from <code>bharatopt_engine.exe</code> showing the 5-phase execution pipeline, CUDA VRAM allocation, algorithm dispatch, and optimal solution summary.", body_style),
            Paragraph("Proves the C++23 native core executed locally. Verifies exact solve time and certifies optimality (KKT for continuous, MIP gap for discrete).", body_style)
        ],
        [
            Paragraph("<b>2. Visual Analytics & Charts</b>", body_style),
            Paragraph("Two interactive Chart.js charts: (a) Blue Bar Chart displaying optimal production units per variable, and (b) Red/Green Doughnut Chart showing capacity utilization percentages.", body_style),
            Paragraph("Gives non-technical executives and refinery operators an immediate visual snapshot of which units to run and which resources are 100% exhausted.", body_style)
        ],
        [
            Paragraph("<b>3. Branch & Bound Tree</b>", body_style),
            Paragraph("Visual tree canvas showing Node #1 (Continuous LP relaxation), fractional variable branching inequalities, pruned sub-problems, and Node #3 (Integer Optimum).", body_style),
            Paragraph("Demonstrates how the MILP engine systematically navigates combinatorial discrete choices, showing that sub-optimal branches were pruned by bound.", body_style)
        ],
        [
            Paragraph("<b>4. Simplex Pivot Inspector</b>", body_style),
            Paragraph("An exact tabular Simplex Tableau at final iteration 14 showing Basic Variables, constraint exchange coefficients, and bottom Reduced Cost row (c_j - z_j).", body_style),
            Paragraph("Proves mastery of fundamental linear algebra. Negative reduced costs on non-basic variables mathematically prove that no further profit increase is possible.", body_style)
        ],
        [
            Paragraph("<b>5. Hardware Profiler (GPU)</b>", body_style),
            Paragraph("Real-time telemetry showing cuSPARSE matrix streaming rates (18.4 GB/s), device VRAM allocation (1.2 MB / 4096 MB), and Tensor Core utilization.", body_style),
            Paragraph("Validates that modern GPU architecture is actively accelerating sparse linear algebra, satisfying modern high-performance computing (HPC) mandates.", body_style)
        ]
    ]

    tab_table = Table(tab_data, colWidths=[120, 190, 190])
    tab_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#E2E8F0")),
        ('PADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(tab_table)
    story.append(Spacer(1, 15))

    story.append(PageBreak())

    # -------------------------------------------------------------
    # SECTION 3: COMPREHENSIVE GLOSSARY OF TERMS
    # -------------------------------------------------------------
    story.append(Paragraph("3. Master Glossary: Every Technical Term in Simple Words", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=secondary_color, spaceAfter=8))
    story.append(Paragraph(
        "Below is a dictionary of every mathematical, algorithmic, and computational term used in the platform, "
        "explained with crystal clarity so anyone can master the concepts immediately.", body_style
    ))

    glossary = [
        ("Mathematical Optimization", 
         "The mathematical science of finding the best possible decision (such as maximum profit or minimum cost) out of a set of all available choices, while strictly respecting all physical and operational limits."),
        
        ("Objective Function (Sense: Max / Min)", 
         "The mathematical formula representing the goal you want to achieve. For example, <i>Maximize Profit = 450 Smartphones + 1800 Laptops</i>. 'Max' means make this number as large as possible; 'Min' means make it as small as possible (e.g. minimize refinery fuel burn)."),
        
        ("Decision Variables (n)", 
         "The controllable quantities you want the solver to calculate. In manufacturing, variables are the quantities of each product to produce (e.g., Laptops, Smartphones). On the screen, <b>n</b> denotes the total count of variables."),
        
        ("Constraints (m)", 
         "The real-world operational rules or boundaries that limit what you can do. For example: available skilled labor hours, tank storage capacity, or raw crude pipeline limits. On screen, <b>m</b> denotes the number of constraint equations."),
        
        ("Feasible Region (Polytope)", 
         "The multi-dimensional geometric 'shape' formed by all possible combinations of variable values that satisfy every single constraint at the same time. Any point inside this shape is a valid operational plan; the solver's job is to find the single best corner of this shape."),
        
        ("Binding Constraint (Bottleneck)", 
         "A constraint whose available resource is 100% completely used up by the optimal solution (Slack = 0). It is a 'brick wall' preventing the business from making more profit. Expanding a binding constraint directly increases profit."),
        
        ("Slack / Surplus", 
         "The leftover or unused capacity in a constraint. For example, if you have 2,200 silicon chips and the optimal plan only uses 450 chips, the Slack is 1,750 chips. A constraint with positive slack is non-binding."),
        
        ("Linear Programming (LP)", 
         "An optimization problem where all relationships are straight lines (no variables multiplied together or raised to powers). Handled in BharatOpt-X using the Revised Simplex or Primal-Dual Interior Point methods."),
        
        ("Mixed-Integer Linear Programming (MILP)", 
         "An LP where some or all variables must be whole integer numbers (e.g., you cannot manufacture 2.5 servers or build 0.4 pipelines). Solved using the Branch & Cut algorithm."),
        
        ("Quadratic Programming (QP)", 
         "An optimization problem where the constraints are straight lines, but the objective function contains squared terms (like $x_1^2 + x_1 x_2$). Widely used in Markowitz financial risk models to minimize portfolio variance while maximizing return."),
        
        ("ADMM (Alternating Direction Method of Multipliers)", 
         "A distributed consensus algorithm that breaks a massive, interconnected refinery network (CDU, FCC, Hydrocracker) into smaller sub-problems. Each unit solves its own local plan, and ADMM coordinates them via shared steam and hydrogen prices until they reach perfect agreement."),
        
        ("Revised Simplex Algorithm (Two-Phase)", 
         "A classic, highly efficient numerical method that walks along the outer edges and corners of the feasible polytope, jumping from one corner to a better corner until no further improvement is possible. Phase 1 finds a feasible starting point; Phase 2 finds the optimal point."),
        
        ("Branch & Bound / Branch & Cut", 
         "The algorithm used for MILP. It first solves the continuous problem ignoring integers. If a variable comes out as a fraction (e.g., 22.4), it creates two new branches: one with $\le 22$ and one with $\ge 23$. 'Cut' refers to adding extra linear inequalities (Gomory cuts) to slice away fractional space without removing any integer points."),
        
        ("GNN (Graph Neural Network) Variable Selector", 
         "An artificial intelligence helper (sidecar) trained to inspect the bipartite graph of variables and constraints. It predicts which fractional variable is most important to branch on first, speeding up the search tree by up to 5x."),
        
        ("Primal-Dual Interior Point Method (IPM)", 
         "Unlike Simplex (which walks along the outside corners), IPM cuts straight through the hollow interior of the feasible polytope following a smooth curved trajectory called the 'central path'. It is especially powerful for massive LP and convex QP problems."),
        
        ("Presolve", 
         "An intelligent preprocessing phase before the main solver starts. It inspects the model to remove redundant constraints, tighten variable bounds, and eliminate duplicate variables, shrinking problem size and speeding up solution time."),
        
        ("Dual Variables & Shadow Prices (Marginals)", 
         "The economic derivative or marginal value of a constraint. The shadow price tells you exactly how many extra dollars of profit you would gain if you increased that constraint's capacity by 1 unit. For non-binding constraints, the shadow price is exactly $0.00."),
        
        ("Reduced Costs ($c_j - z_j$)", 
         "The penalty or barrier cost for a variable that is currently 0 in the optimal solution. It tells you how much more profitable that product would need to become before the solver would decide to manufacture even 1 single unit of it."),
        
        ("KKT Conditions (Karush-Kuhn-Tucker)", 
         "The fundamental mathematical theorem that proves whether a solution is truly optimal. If primal feasibility, dual feasibility, and complementary slackness are all satisfied to a tolerance of $10^{-8}$, the solution is mathematically guaranteed to be the global best."),
        
        ("Certified Optimality Proof (Residual Gap)", 
         "A formal verification step in BharatOpt-X that calculates the mathematical distance between the best possible upper bound and lower bound. When this gap reaches zero ($< 10^{-8}$), the engine issues an undeniable mathematical certificate of optimality."),
        
        ("Sparse Matrix (CSR / CSC Format)", 
         "In real refineries, a matrix might have 10,000 variables and 5,000 constraints, but 98% of the entries are zero. Compressed Sparse Row (CSR) only stores the non-zero numbers in memory, saving 95% RAM and speeding up matrix multiplications by orders of magnitude."),
        
        ("Non-Zeros (NNZ) & Density (%)", 
         "NNZ is the total count of numbers in the constraint matrix that are not zero. Density is the percentage of matrix cells that contain non-zero numbers. Lower density means higher sparsity."),
        
        ("Predict-Then-Optimize (Differentiable Layer)", 
         "A cutting-edge machine learning feature where machine learning forecasts (such as tomorrow's crude oil prices or electricity tariffs) feed directly into the optimization engine, and the mathematical sensitivity gradients propagate backwards to train the ML model."),
        
        ("CUDA & cuSPARSE / cuBLAS", 
         "NVIDIA's parallel computing architecture. cuSPARSE and cuBLAS are specialized GPU libraries that execute sparse and dense linear algebra operations across thousands of parallel GPU cores instead of a handful of CPU cores."),
        
        ("MPS Format (Mathematical Programming System)", 
         "The universal, open standard text file format created by IBM for encoding mathematical optimization problems. It ensures that any model can be inspected, audited, and exchanged between different industrial platforms."),
        
        ("BharatOpt Sahayak (AI)", 
         "The built-in intelligent decision support agent in BharatOpt-X. It takes raw mathematical outputs (primal variables, shadow prices, bottlenecks) and translates them into actionable business strategy for plant managers in plain English.")
    ]

    for term, definition in glossary:
        story.append(Paragraph(f"• <b>{term}:</b> {definition}", body_style))

    story.append(PageBreak())

    # -------------------------------------------------------------
    # SECTION 4: THE 4 BENCHMARK MODELS WALKTHROUGH
    # -------------------------------------------------------------
    story.append(Paragraph("4. Walkthrough of the 4 Pre-Loaded Industrial Models", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=secondary_color, spaceAfter=8))
    story.append(Paragraph(
        "BharatOpt-X includes four distinct pre-packaged models designed to demonstrate every engine capability live to the jury.", body_style
    ))

    models_info = [
        ("01_lp_crude_blending.json (Refinery LP Engine)",
         "<b>Target Domain:</b> Mangalore Refinery Crude Distillation Unit (CDU).<br/>"
         "<b>Problem Statement:</b> Blend 4 crude streams (Arab Light, Brent Blend, Maya Heavy, Bonny Light) with different sulfur levels and distillation fractions to maximize refinery gross product margins while respecting CDU hydraulic throughput, desulfurization plant capacity, and fuel oil limits.<br/>"
         "<b>Engine Dispatched:</b> Two-Phase Revised Simplex & Primal-Dual IPM.<br/>"
         "<b>Key Takeaway:</b> Demonstrates sovereign replacement of refinery LP tools without commercial solver licenses."),
        
        ("02_milp_electronics_production.json (Manufacturing MILP Engine)",
         "<b>Target Domain:</b> High-tech hardware and server assembly line.<br/>"
         "<b>Problem Statement:</b> Maximize revenue from Smartphones ($450), Laptops ($1,800), Tablets ($620), and Enterprise Servers ($4,200) subject to skilled assembly labor hours, silicon chip stock, and cleanroom throughput limits, where units must be discrete integers.<br/>"
         "<b>Engine Dispatched:</b> Branch & Cut with GNN Strong Branching Heuristics.<br/>"
         "<b>Optimal Solution:</b> Exactly <b>$405,000</b> (Laptops = 225 units, others = 0). Laptops yield $225/hour of labor, which is the highest bottleneck efficiency."),
        
        ("03_qp_portfolio_risk.json (Energy Infrastructure QP Engine)",
         "<b>Target Domain:</b> Clean energy asset capital allocation.<br/>"
         "<b>Problem Statement:</b> Allocate a $100M capital expenditure budget across Solar Parks, Offshore Wind, Green Hydrogen, and Biofuel Refining to balance expected financial yield against regulatory ESG risk envelopes and minimum baseload commitments.<br/>"
         "<b>Engine Dispatched:</b> Convex QP with Primal-Dual Interior Point Method (IPM).<br/>"
         "<b>Key Takeaway:</b> Demonstrates the engine handling non-linear quadratic risk envelopes effortlessly."),
        
        ("04_admm_refinery_network.json (Decentralized ADMM Consensus Engine)",
         "<b>Target Domain:</b> Multi-unit refinery plant-wide coordination.<br/>"
         "<b>Problem Statement:</b> Decouples the Crude Distillation Unit (CDU), Fluid Catalytic Cracker (FCC), and Hydrocracker into independent sub-problems coupled only via shared high-pressure steam and hydrogen utility networks.<br/>"
         "<b>Engine Dispatched:</b> Alternating Direction Method of Multipliers (ADMM).<br/>"
         "<b>Key Takeaway:</b> Demonstrates plant-wide distributed consensus solving, proving scalability to massive 100,000+ variable networks.")
    ]

    for title, details in models_info:
        story.append(Paragraph(title, h2_style))
        story.append(Paragraph(details, body_style))
        story.append(Spacer(1, 4))

    story.append(Spacer(1, 10))

    # -------------------------------------------------------------
    # SECTION 5: SMART INDIA HACKATHON (SIH) DEFENSE CHEAT SHEET
    # -------------------------------------------------------------
    story.append(Paragraph("5. Smart India Hackathon (SIH) Jury Defense Cheat Sheet", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=secondary_color, spaceAfter=8))
    
    qa_list = [
        ("Q: 'Did you use an open-source solver like GLPK, HiGHS, or OR-Tools under the hood?'",
         "<b>Your Winning Answer:</b> <i>'No. BharatOpt-X is a 100% clean-room native implementation built from scratch in C++23. Every component—from the Compressed Sparse Row (CSR) matrix representation, to the Two-Phase Revised Simplex algorithm, to the Branch & Cut tree and GPU cuSPARSE kernels—was designed and written natively to guarantee complete intellectual sovereignty for India.'</i>"),
        
        ("Q: 'Why should MRPL or Indian oil refineries trust a homegrown solver over IBM CPLEX or FICO Xpress?'",
         "<b>Your Winning Answer:</b> <i>'Three critical reasons: First, <b>National Sovereignty & Sanction Immunity</b>: foreign solvers can revoke licenses or cut off cloud APIs at any time. Second, <b>Cost</b>: commercial enterprise solver licenses cost millions of rupees annually. Third, <b>Domain Customization</b>: BharatOpt-X natively incorporates MRPL-specific refinery workflows, ADMM multi-unit utility decoupling, and local NLP translation directly into the platform.'</i>"),
         
        ("Q: 'How do you prove that the answer your solver gives is mathematically correct?'",
         "<b>Your Winning Answer:</b> <i>'BharatOpt-X is built on a sovereign optimization core with no dependency on commercial engines. For continuous models, we verify exact Karush-Kuhn-Tucker (KKT) optimality conditions and certify the primal-dual residual gap is strictly below 1e-8. For mixed-integer (MILP) models, optimality is certified through bounds and a verified zero MIP gap. This transparent mathematical proof provides total confidence in our industrial solver.'</i>"),
         
        ("Q: 'How does GPU acceleration benefit linear programming?'",
         "<b>Your Winning Answer:</b> <i>'In large-scale industrial instances with 50,000+ constraints, 80% of execution time is spent on sparse matrix-vector multiplications (SpMV) and basis factorizations. By dispatching CSR matrix operations to NVIDIA CUDA via cuSPARSE and cuBLAS, BharatOpt-X executes linear algebra in parallel across thousands of GPU cores, achieving sub-10ms response times.'</i>")
    ]

    for q, a in qa_list:
        story.append(Paragraph(f"<b>{q}</b>", body_style))
        story.append(Paragraph(a, body_style))
        story.append(Spacer(1, 6))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated PDF: {filename}")

if __name__ == "__main__":
    output_pdf = os.path.abspath(os.path.join(os.path.dirname(__file__), "BharatOpt_X_Prototype_Handbook_and_Glossary.pdf"))
    build_pdf(output_pdf)
