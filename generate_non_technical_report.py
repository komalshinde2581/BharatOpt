import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def generate_pdf():
    pdf_file = "BharatOpt_X_Non_Technical_Guide.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50)
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=14,
        textColor=colors.HexColor('#1E3A8A'),
        alignment=1 # Center
    )
    
    chapter_style = ParagraphStyle(
        'ChapterStyle',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=12,
        spaceAfter=8,
        textColor=colors.HexColor('#0F172A'),
        backColor=colors.HexColor('#F1F5F9'),
        borderPadding=5
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=10,
        leading=16
    )
    
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontSize=11,
        leftIndent=20,
        spaceAfter=8,
        leading=15
    )

    story = []

    # Title
    story.append(Paragraph("BharatOpt-X: Non-Technical Executive Summary & Guide", title_style))
    story.append(Spacer(1, 10))

    # 1. Introduction
    story.append(Paragraph("1. What is BharatOpt-X? (The Big Picture)", chapter_style))
    intro_text = (
        "<b>BharatOpt-X</b> is an advanced software engine built to solve extremely complex 'optimization' problems. "
        "In simple terms, optimization means finding the absolute best way to do something when you have limited resources. "
        "For example, how should a crude oil refinery mix different chemicals to maximize their profit, while making sure "
        "they don't exceed their storage limits and meet strict environmental rules?<br/><br/>"
        "Previously, Indian companies and the government relied on expensive foreign software (like Gurobi or CPLEX) "
        "to do this math. BharatOpt-X is a 'Sovereign' (indigenous/home-grown) alternative. It runs entirely on local computers, "
        "meaning sensitive data never leaves the organization, and it does not require millions of dollars in licensing fees."
    )
    story.append(Paragraph(intro_text, body_style))

    # 2. The Workflow
    story.append(Paragraph("2. How It Works (The Step-by-Step Workflow)", chapter_style))
    story.append(Paragraph("When a user wants to solve a problem, BharatOpt-X goes through a highly organized pipeline:", body_style))
    
    workflows = [
        "<b>Step 1: Model Ingestion:</b> The user uploads a file describing their business problem (like resources, costs, and limits).",
        "<b>Step 2: The Classifier:</b> The system's brain analyzes the problem and decides what kind of math is needed. Is it a simple straight-line problem (Linear), or does it involve whole numbers like 'buying exactly 3 ships, not 3.5' (Mixed-Integer)?",
        "<b>Step 3: Hardware Acceleration:</b> The engine connects to the computer's Graphics Card (GPU). GPUs are incredibly fast at doing thousands of small math problems at the exact same time, acting like a turbocharger.",
        "<b>Step 4: The Core Math Engine:</b> The C++ engine cranks through millions of possibilities using advanced algorithms (like 'Branch-and-Bound') to definitively prove it has found the best possible answer.",
        "<b>Step 5: Decision Support:</b> Instead of just spitting out raw numbers, a 'Decision Support Layer' translates the math back into plain English (e.g., 'To maximize profit, run Unit A at 80% capacity')."
    ]
    for w in workflows:
        story.append(Paragraph(f"• {w}", bullet_style))

    # 3. Technologies Used
    story.append(Paragraph("3. Technologies Used (Under the Hood)", chapter_style))
    story.append(Paragraph("BharatOpt-X uses a mix of different programming languages, each chosen for a specific strength:", body_style))
    
    techs = [
        "<b>C++23 (The Heavy Lifter):</b> C++ is known for being blazingly fast. All the complex math, searching through trees of possibilities, and number crunching happens here.",
        "<b>Python & FastAPI (The Bridge):</b> Python is great for moving data around. It takes the problem from the web browser, hands it to the C++ engine, and carries the answer back.",
        "<b>JavaScript, HTML, CSS (The Face):</b> These build the visual dashboard you see in your web browser. It makes the system user-friendly so you don't have to be a coder to use it.",
        "<b>CUDA / GPU (The Turbocharger):</b> A technology by NVIDIA that lets our math engine use the computer's graphics card to do massive calculations instantly."
    ]
    for t in techs:
        story.append(Paragraph(f"• {t}", bullet_style))

    # 4. Homescreen Terms
    story.append(Paragraph("4. Understanding the Homescreen", chapter_style))
    story.append(Paragraph("When you look at the web dashboard, you will see several technical terms. Here is what they actually mean:", body_style))

    ui_terms = [
        "<b>Upload JSON/MPS:</b> The door to give the system your problem. JSON and MPS are just file formats that list out your costs, profits, and limits.",
        "<b>Solve Model:</b> The start button that kicks off the C++ math engine.",
        "<b>Objective Value:</b> The final answer. If you asked the system to maximize profit, this number is your maximum possible profit.",
        "<b>Solver Status: Optimal:</b> The engine's guarantee. It means it hasn't just found a 'good' answer, it has mathematically proven that it is impossible to find a better answer.",
        "<b>Solver Status: Infeasible:</b> The engine's warning. It means you gave it an impossible task (e.g., 'Make $10,000 but you can only spend $5').",
        "<b>Phase 1 / Phase 2 Iterations:</b> How many mathematical steps (pivots) the engine took to narrow down the answer.",
        "<b>Nodes Explored:</b> When dealing with whole numbers (like 3 ships, not 3.5), the engine guesses different scenarios. A 'node' is one of those scenarios. This shows how many it checked.",
        "<b>MIP Gap:</b> The 'Margin of Error' for whole-number problems. If it says 0.0%, the answer is perfect. If it says 2%, it means the system found a great answer, but there *might* be an answer 2% better hidden somewhere.",
        "<b>Best Bound:</b> The theoretical absolute limit. Even if the engine hasn't found the perfect answer yet, it knows the answer can never be better than this 'Best Bound' number.",
        "<b>Decision Support Advice:</b> The AI translator. It reads the raw math and tells the human operator exactly what actions to take in plain English."
    ]
    for u in ui_terms:
        story.append(Paragraph(f"• {u}", bullet_style))

    # 5. The Value Proposition
    story.append(Paragraph("5. Why This Matters (The Value Proposition)", chapter_style))
    val_text = (
        "By building this completely from scratch (Native C++ Engine) rather than wrapping around existing tools, "
        "BharatOpt-X provides true Digital Sovereignty. It proves that complex industrial optimization can be done "
        "without paying massive recurring fees to foreign software monopolies, while keeping critical national infrastructure "
        "data completely secure and offline."
    )
    story.append(Paragraph(val_text, body_style))

    # Build PDF
    doc.build(story)
    print(f"Report successfully generated at: {pdf_file}")

if __name__ == "__main__":
    generate_pdf()
