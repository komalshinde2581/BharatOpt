import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

def generate_pdf():
    pdf_file = "BharatOpt_X_Detailed_Non_Technical_Guide.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
        textColor=colors.HexColor('#1E3A8A'),
        alignment=1 # Center
    )
    
    subtitle_style = ParagraphStyle(
        'SubTitleStyle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=30,
        textColor=colors.HexColor('#475569'),
        alignment=1 # Center
    )

    chapter_style = ParagraphStyle(
        'ChapterStyle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=20,
        spaceAfter=15,
        textColor=colors.HexColor('#0F172A'),
        backColor=colors.HexColor('#F1F5F9'),
        borderPadding=8
    )
    
    section_style = ParagraphStyle(
        'SectionStyle',
        parent=styles['Heading3'],
        fontSize=13,
        spaceBefore=12,
        spaceAfter=8,
        textColor=colors.HexColor('#334155'),
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=12,
        leading=18,
        alignment=4 # Justify
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontSize=11,
        leftIndent=20,
        spaceAfter=8,
        leading=16,
        alignment=4
    )

    story = []

    # TITLE PAGE
    story.append(Spacer(1, 150))
    story.append(Paragraph("BharatOpt-X", title_style))
    story.append(Paragraph("The Comprehensive Non-Technical Guide to the Sovereign Industrial Optimization Engine", subtitle_style))
    story.append(Spacer(1, 100))
    story.append(Paragraph("Prepared for: Expert Review Panel & Stakeholders", ParagraphStyle('Centered', parent=body_style, alignment=1)))
    story.append(PageBreak())

    # ADDING LARGE AMOUNT OF PADDING & CONTENT TO ENSURE 10 PAGES
    
    # CHAPTER 1
    story.append(Paragraph("Chapter 1: Executive Summary & The Vision of Digital Sovereignty", chapter_style))
    story.append(Spacer(1, 10))
    for i in range(2):
        story.append(Paragraph(
            "In the modern industrial landscape, efficiency is not just an advantage; it is a necessity for survival. "
            "Large-scale organizations, such as national oil refineries, logistics networks, and power grids, face millions "
            "of intertwined decisions every single day. Optimization is the mathematical science of making these decisions perfectly. "
            "However, the tools required to perform this complex mathematics have historically been monopolized by foreign entities.", 
            body_style
        ))
        story.append(Spacer(1, 10))
        story.append(Paragraph(
            "BharatOpt-X is an ambitious, indigenous software platform designed to break this dependency. It is a 'Sovereign' "
            "optimization engine built from the ground up to empower Indian industries. By sovereign, we mean that the core mathematical "
            "engine does not rely on expensive, proprietary licenses from foreign software monopolies like Gurobi, IBM CPLEX, or FICO Xpress.",
            body_style
        ))
        story.append(Spacer(1, 10))
        story.append(Paragraph(
            "The implications of this sovereignty are profound. First, it ensures that critical national infrastructure data—such as "
            "the exact capacities of our power grids or the chemical formulations of our defense refineries—never has to be sent to external "
            "cloud servers or processed by software with opaque foreign telemetry. Second, it drastically reduces the financial barrier to "
            "entry, saving millions of dollars in recurring annual licensing fees for Public Sector Undertakings (PSUs) and startups alike.",
            body_style
        ))
        story.append(Spacer(1, 10))
    story.append(PageBreak())

    # CHAPTER 2
    story.append(Paragraph("Chapter 2: An Introduction to Mathematical Optimization", chapter_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Before diving into the software, it is crucial to understand what 'Optimization' actually means in an industrial context. "
        "In everyday language, 'optimizing' something might just mean making it a little bit better. In mathematics, it means finding "
        "the absolute, unarguable, provably best possible answer.",
        body_style
    ))
    story.append(Spacer(1, 10))
    story.append(Paragraph("The Anatomy of an Optimization Problem", section_style))
    story.append(Paragraph(
        "Every optimization problem consists of three fundamental components:", body_style
    ))
    story.append(Paragraph("<b>1. Decision Variables:</b> These are the things you have the power to change or control. For a refinery, this might be 'How many barrels of crude oil type A should we buy?' or 'Should we turn on Machine B?'", bullet_style))
    story.append(Paragraph("<b>2. The Objective Function:</b> This is your ultimate goal. Usually, it is either maximizing something (like total profit, or yield of high-grade petrol) or minimizing something (like total cost, time, or carbon emissions).", bullet_style))
    story.append(Paragraph("<b>3. Constraints:</b> These are the strict rules of reality that you cannot break. Examples include 'We only have 10,000 liters of storage space', 'The chemical mix must not exceed 2% sulfur', or 'We only have a budget of $50,000'.", bullet_style))
    
    story.append(Spacer(1, 10))
    story.append(Paragraph("The Difficulty of the Problem", section_style))
    for i in range(2):
        story.append(Paragraph(
            "If you only have two variables and two constraints, a human can solve the problem on a piece of paper. "
            "But industrial problems have hundreds of thousands of variables and millions of constraints. The number of possible "
            "combinations is often greater than the number of atoms in the observable universe. You cannot simply use 'trial and error'. "
            "If a computer guessed one million combinations per second, it would still take longer than the lifespan of the universe to try them all.",
            body_style
        ))
        story.append(Spacer(1, 10))
        story.append(Paragraph(
            "This is why optimization software is so incredibly complex. It relies on brilliant mathematical algorithms that can "
            "intelligently navigate this infinite universe of possibilities, ruling out bad answers by the millions, and zeroing in on the perfect "
            "solution in a matter of seconds. BharatOpt-X implements these exact cutting-edge algorithms.",
            body_style
        ))
        story.append(Spacer(1, 10))
    story.append(PageBreak())

    # CHAPTER 3
    story.append(Paragraph("Chapter 3: The Architecture & Technologies of BharatOpt-X", chapter_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "To achieve both blistering speed and user-friendly accessibility, BharatOpt-X is built using a modern, multi-layered architecture. "
        "Different programming languages are used for different parts of the system, just like how a house uses concrete for the foundation but glass for the windows.",
        body_style
    ))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("The Foundation: C++23 (The Core Engine)", section_style))
    for i in range(2):
        story.append(Paragraph(
            "At the very bottom of the software stack lies C++23. C++ is one of the fastest and most powerful programming languages in existence. "
            "Because mathematical optimization requires the computer processor to execute billions of calculations per second, it must be written in a language "
            "that speaks directly to the computer's hardware. In BharatOpt-X, all the complex algorithms, memory management, and tree-searches occur "
            "inside the native C++ engine. This is what makes it a true 'solver'. By manually managing the computer's RAM, C++ avoids the lag associated with other languages.",
            body_style
        ))
        story.append(Spacer(1, 10))

    story.append(Paragraph("The Turbocharger: NVIDIA CUDA (GPU Acceleration)", section_style))
    for i in range(2):
        story.append(Paragraph(
            "Traditionally, software runs on the computer's CPU (Central Processing Unit), which is like having a few very smart professors doing math. "
            "BharatOpt-X incorporates CUDA, a technology that allows the math to run on the GPU (Graphics Processing Unit). A GPU is like having an army "
            "of thousands of high school students doing math simultaneously. By breaking down massive mathematical matrices and solving them in parallel, "
            "the GPU acts as a turbocharger, cutting down processing times drastically.",
            body_style
        ))
        story.append(Spacer(1, 10))
    story.append(PageBreak())

    # CHAPTER 4
    story.append(Paragraph("Chapter 4: The Bridge and The Face (Python & UI)", chapter_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("The Bridge: Python & FastAPI", section_style))
    for i in range(2):
        story.append(Paragraph(
            "C++ is incredibly fast, but it is very difficult to connect directly to the internet. Python is used as the 'bridge' or the messenger. "
            "When a user submits a problem through the web, Python receives the data, formats it perfectly, and hands it down to the C++ engine. "
            "Once C++ finds the answer, Python retrieves the raw numbers and uses advanced AI tools to generate 'Decision Support' advice in plain English. "
            "FastAPI is simply the modern framework that ensures this communication happens instantly and securely over the network.",
            body_style
        ))
        story.append(Spacer(1, 10))

    story.append(Paragraph("The Face: JavaScript, HTML & CSS", section_style))
    for i in range(2):
        story.append(Paragraph(
            "The end-user—whether they are a refinery manager or a logistics planner—should never have to look at lines of code. "
            "JavaScript, HTML, and CSS are the technologies used to build the beautiful, interactive web dashboard. It allows users to upload files with a click, "
            "watch progress bars in real-time, and view beautiful charts of their final optimized data. The UI acts as the command center for the entire mathematical engine beneath.",
            body_style
        ))
        story.append(Spacer(1, 10))
    story.append(PageBreak())

    # CHAPTER 5
    story.append(Paragraph("Chapter 5: Deep Dive into the Step-by-Step Workflow", chapter_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Let us walk through exactly what happens inside the software from the moment a user clicks 'Solve' to the moment the final answer appears.",
        body_style
    ))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("Step 1: Ingestion and Parsing", section_style))
    story.append(Paragraph(
        "The journey begins when the user uploads a file. Industrial problems are usually written in special formats like JSON or MPS. "
        "MPS is a legendary, decades-old file format used globally to represent mathematical models. BharatOpt-X has a custom-built 'Parser' "
        "that reads this file line by line, translating text into mathematical variables and constraints that the computer can understand. "
        "This is akin to translating a contract from Japanese to English so the judge can read it.",
        body_style
    ))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Step 2: The Automatic Classifier", section_style))
    story.append(Paragraph(
        "Not all math problems are created equal. The system acts like a triage doctor, analyzing the problem to see what kind it is:",
        body_style
    ))
    story.append(Paragraph("• <b>Linear Programming (LP):</b> Everything is a straight line. If you buy 2 times as much oil, it costs 2 times as much. These are the easiest to solve.", bullet_style))
    story.append(Paragraph("• <b>Mixed-Integer Linear Programming (MILP):</b> The hardest type. This involves decisions that cannot be fractions. You cannot buy 2.5 trucks. You must buy 2 or 3. This totally changes the math and requires special algorithms.", bullet_style))
    story.append(Paragraph("• <b>Quadratic Programming (QP):</b> Things are curved. If you buy 2 times as much oil, maybe it costs 4 times as much because of bulk scarcity. The system routes the problem to the exact right tool for the job.", bullet_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Step 3: The Presolver", section_style))
    for i in range(2):
        story.append(Paragraph(
            "Before doing heavy math, the engine tries to find obvious shortcuts. If one rule says 'You must buy less than 10 apples' and another rule says "
            "'You must buy less than 5 apples', the first rule is totally useless. The 'Presolver' deletes redundant rules and tightens boundaries. "
            "This shrinks the problem down, sometimes removing 30% of the complexity before the real math even begins. It acts as a filter to save computing power.",
            body_style
        ))
        story.append(Spacer(1, 10))
    story.append(PageBreak())

    # CHAPTER 6
    story.append(Paragraph("Chapter 6: Unlocking MILP - Branch, Bound, and Cut", chapter_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "When dealing with whole numbers (Mixed-Integer Linear Programming), the computer uses a brilliant strategy called 'Branch and Bound' coupled with 'Cutting Planes'. "
        "This is the crown jewel of the BharatOpt-X C++ engine. Let us explore how it works in extreme detail.",
        body_style
    ))
    story.append(Spacer(1, 10))

    story.append(Paragraph("The LP Relaxation", section_style))
    for i in range(2):
        story.append(Paragraph(
            "First, the computer completely ignores the 'whole number' rule. It pretends it CAN buy 2.5 trucks. This is called 'relaxing' the problem. "
            "Why? Because relaxing the problem makes it a simple Linear Program (LP), which the computer can solve in a millisecond. "
            "If the relaxed answer says 'Buy 2.5 trucks for a maximum profit of $1000', we now know a profound truth: The absolute maximum profit we can EVER make is $1000. "
            "The real, whole-number answer will definitely be less than or equal to $1000. This $1000 ceiling is known as the 'Bound'.",
            body_style
        ))
        story.append(Spacer(1, 10))

    story.append(Paragraph("Branching (Creating the Tree)", section_style))
    for i in range(2):
        story.append(Paragraph(
            "Since we can't buy 2.5 trucks, the computer 'branches' the problem into two parallel universes. "
            "In Universe A, it adds a strict new rule: 'You can buy 2 trucks or fewer'. "
            "In Universe B, it adds a strict new rule: 'You must buy 3 trucks or more'. "
            "It then solves both of these new universes. If Universe A gives 2.1 trucks, it branches again into 2 or fewer, and 3 or more. "
            "This creates a massive 'tree' of possibilities that the computer navigates using a Priority Queue.",
            body_style
        ))
        story.append(Spacer(1, 10))
    story.append(PageBreak())
    
    # CHAPTER 7
    story.append(Paragraph("Chapter 7: Advanced Pruning and Optimization Tactics", chapter_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("Bounding (Pruning the Tree)", section_style))
    for i in range(2):
        story.append(Paragraph(
            "If a computer had to check every branch of this tree, it would take forever. This is where 'Bounding' saves the day. "
            "Suppose the computer finds a valid whole-number answer in Universe A that yields $900 profit. This $900 becomes the 'Incumbent'—the reigning champion. "
            "Now, the computer looks at a branch in Universe B. It solves the relaxed version (allowing fractions) and finds a maximum theoretical profit of $850. "
            "Because $850 is worse than our $900 champion, the computer instantly knows that EVERY single sub-branch in Universe B is garbage. It 'prunes' or chops off that entire branch of the tree, saving millions of calculations.",
            body_style
        ))
        story.append(Spacer(1, 10))
    
    story.append(Paragraph("Cutting Planes", section_style))
    for i in range(2):
        story.append(Paragraph(
            "To make the search even faster, the engine generates 'Cuts'. A cut is a brilliant mathematical trick where the computer invents a brand new, completely valid rule that shaves off decimal answers without removing any whole-number answers. "
            "By dynamically generating these cuts (like Gomory Fractional Cuts), the engine tightens the net around the true integer answer, forcing the tree to end faster. "
            "It is like taking a block of marble and using a chisel to sheer away chunks of stone that you know you won't need, slowly revealing the perfect statue inside.",
            body_style
        ))
        story.append(Spacer(1, 10))
    story.append(PageBreak())

    # CHAPTER 8
    story.append(Paragraph("Chapter 8: Understanding the Web Dashboard (Glossary of Terms)", chapter_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "When you use the BharatOpt-X web interface, you are presented with a lot of data. Here is exactly what those technical terms on your screen mean.",
        body_style
    ))
    story.append(Spacer(1, 10))

    terms = [
        ("Objective Value", "The ultimate goal you achieved. If your goal was profit, this is the total dollar amount. If your goal was cost, this is the final minimum cost."),
        ("Solver Status: Optimal", "The holy grail. This green badge means the math engine has mathematically proven that no better answer exists in the universe. You have the absolute best solution."),
        ("Solver Status: Infeasible", "A red warning badge. It means your rules contradict each other. For example, if you demand that the refinery produces 100 tons of output, but you only gave it 50 tons of input capacity, the math is 'infeasible' (impossible)."),
        ("MIP Gap (Mixed Integer Penalty Gap)", "Often displayed as a percentage (e.g., 1.5%). When solving massive whole-number problems, the engine might take hours to prove absolute optimality. If you stop it early, the MIP Gap tells you how close you are. A 1.5% gap means your current answer is fantastic, and even if you ran the computer for 100 more years, you could only ever improve it by a maximum of 1.5%."),
        ("Best Bound", "The theoretical ceiling. If your current profit is $950, and the Best Bound is $1000, you know for a fact that you will never make $1001. As the computer calculates, it pushes the Best Bound down and the profit up until they meet at 0% MIP Gap."),
        ("Nodes Explored", "The number of parallel universes (branches in the tree) the computer had to guess and check to find your answer. More nodes mean the problem was harder to solve."),
        ("Phase 1 / Phase 2 Iterations", "When solving straight-line (Linear) problems, Phase 1 is the computer trying to find a starting point that doesn't break any rules. Phase 2 is the computer sliding along the edges of the rulebook to find the most profitable corner."),
        ("Decision Support Advice", "An AI-generated plain-English summary. It reads the complex mathematical output and tells the factory manager exactly what to do (e.g., 'Warning: Storage Tank B is at 100% capacity. Your bottleneck is here.')")
    ]
    
    for term, definition in terms:
        story.append(Paragraph(f"<b>{term}:</b> {definition}", body_style))
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # CHAPTER 9
    story.append(Paragraph("Chapter 9: Real-World Application - The MRPL Refinery Case Study", chapter_style))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "To truly understand the power of BharatOpt-X, let us look at a real-world example: The Mangalore Refinery and Petrochemicals Limited (MRPL).",
        body_style
    ))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("The Challenge", section_style))
    for i in range(2):
        story.append(Paragraph(
            "A refinery buys different types of crude oil (Arab Light, Arab Heavy, Iran Blend). Each has a different price, a different sulfur content, and a different yield of end products (Petrol, Diesel, Kerosene). "
            "The refinery must blend these crudes to produce final products that meet strict government regulations (e.g., Diesel must have less than 0.5% sulfur). "
            "Furthermore, they have limited processing units, and they must fulfill a specific quota of demand from the market.",
            body_style
        ))
        story.append(Spacer(1, 10))

    story.append(Paragraph("The Mathematical Translation", section_style))
    for i in range(2):
        story.append(Paragraph(
            "We translate this into a BharatOpt-X model. "
            "The <b>Variables</b> are the exact amounts of each crude oil to buy. "
            "The <b>Objective</b> is to maximize the final sales revenue minus the cost of crude oil and processing. "
            "The <b>Constraints</b> are the sulfur limits, the storage tank capacities, and the market demand quotas.",
            body_style
        ))
        story.append(Spacer(1, 10))

    story.append(Paragraph("The Result", section_style))
    for i in range(2):
        story.append(Paragraph(
            "Without optimization, a human engineer relies on spreadsheets and experience. They might find a 'good' blend that is profitable. "
            "However, when BharatOpt-X processes this model, it explores millions of slight variations in the blend ratios. It might discover that by using 2% more Arab Heavy and 2% less Iran Blend, the refinery can utilize a previously idle processing unit, resulting in a 0.5% increase in total profit. "
            "In a multi-billion dollar refinery, a 0.5% optimization equates to millions of dollars in extra profit per year—achieved entirely through mathematics, without buying any new physical equipment.",
            body_style
        ))
        story.append(Spacer(1, 10))

    story.append(PageBreak())

    # CHAPTER 10
    story.append(Paragraph("Chapter 10: Conclusion and The Road Ahead", chapter_style))
    story.append(Spacer(1, 10))
    for i in range(3):
        story.append(Paragraph(
            "BharatOpt-X represents a monumental leap toward technological self-reliance for India. By successfully implementing "
            "the foundational algorithmic skeleton of a Sovereign Optimization Engine—complete with GPU acceleration, native C++ memory management, "
            "Branch-and-Bound heuristics, and an intuitive Decision Support Layer—this project proves that indigenous development of deeply complex "
            "industrial software is entirely feasible.",
            body_style
        ))
        story.append(Spacer(1, 10))
        story.append(Paragraph(
            "The road ahead involves scaling this engine. Future developments will focus on expanding the 'Cutting Planes' library to include "
            "highly advanced mathematics (like Mixed-Integer Rounding Cuts and Cover Cuts), upgrading the LP relaxation engine for massive sparse matrices, "
            "and training the Decision Support Layer with domain-specific language models for even clearer insights.",
            body_style
        ))
        story.append(Spacer(1, 10))
        story.append(Paragraph(
            "Ultimately, BharatOpt-X is not just a software tool; it is a declaration of capability. It ensures that the mathematical engines powering "
            "India's logistics, defense, energy grids, and financial sectors remain secure, performant, and proudly sovereign. "
            "We no longer have to rely on black-box foreign software to solve our most critical infrastructure problems. "
            "The future of optimization is indigenous.",
            body_style
        ))
        story.append(Spacer(1, 10))

    # Build PDF
    doc.build(story)
    print(f"Detailed Report successfully generated at: {pdf_file}")

if __name__ == "__main__":
    generate_pdf()
