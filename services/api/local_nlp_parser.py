import re

def parse_to_mps(text: str) -> str:
    """
    Local, deterministic parser that converts structured English algebraic 
    optimization formulations directly into standard MPS format.
    No external LLM or API is used, preserving absolute data sovereignty.
    """
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    obj_name = "OBJ"
    obj_terms = {}
    obj_sense = "max"
    constraints = []
    
    mode = None
    for line in lines:
        upper = line.upper()
        if upper.startswith("MAXIMIZE"):
            mode = "OBJ"
            obj_sense = "max"
            continue
        elif upper.startswith("MINIMIZE"):
            mode = "OBJ"
            obj_sense = "min"
            continue
        elif upper.startswith("SUBJECT TO") or upper.startswith("CONSTRAINTS"):
            mode = "CONS"
            continue
            
        if mode == "OBJ":
            # Parse terms like "10 Chairs + 20 Tables"
            terms = re.findall(r'([+-]?\s*\d*\.?\d*)\s*([A-Za-z0-9_]+)', line)
            for coef, var in terms:
                c = coef.replace(' ', '')
                if c == '+' or c == '': c = '1'
                elif c == '-': c = '-1'
                obj_terms[var] = float(c)
                
        elif mode == "CONS":
            # Parse constraints like "Labor: 2 Chairs + 3 Tables <= 100"
            if ':' in line:
                c_name, expr = line.split(':', 1)
            else:
                c_name = f"C{len(constraints)+1}"
                expr = line
                
            c_name = c_name.strip()
            
            # Check relational operator
            rel = "L"
            rhs = 0.0
            if "<=" in expr:
                left, right = expr.split("<=")
                rel = "L"
            elif ">=" in expr:
                left, right = expr.split(">=")
                rel = "G"
            elif "=" in expr:
                left, right = expr.split("=")
                rel = "E"
            else:
                continue # Skip invalid format
                
            rhs = float(right.strip())
            
            c_terms = {}
            terms = re.findall(r'([+-]?\s*\d*\.?\d*)\s*([A-Za-z0-9_]+)', left)
            for coef, var in terms:
                c = coef.replace(' ', '')
                if c == '+' or c == '': c = '1'
                elif c == '-': c = '-1'
                c_terms[var] = float(c)
                
            constraints.append({"name": c_name, "rel": rel, "rhs": rhs, "terms": c_terms})
            
    # Generate MPS string dynamically
    mps = []
    mps.append("NAME          LOCAL_MODEL")
    mps.append("ROWS")
    mps.append(f" N  {obj_name}")
    for c in constraints:
        mps.append(f" {c['rel']}  {c['name']}")
        
    mps.append("COLUMNS")
    
    # Extract unique variables
    all_vars = set(obj_terms.keys())
    for c in constraints:
        all_vars.update(c['terms'].keys())
        
    for var in sorted(all_vars):
        if var in obj_terms:
            mps.append(f"    {var:<10} {obj_name:<10} {obj_terms[var]}")
        for c in constraints:
            if var in c['terms']:
                mps.append(f"    {var:<10} {c['name']:<10} {c['terms'][var]}")
                
    mps.append("RHS")
    for c in constraints:
        mps.append(f"    RHS1      {c['name']:<10} {c['rhs']}")
        
    mps.append("BOUNDS")
    for var in sorted(all_vars):
        mps.append(f" LO BND       {var:<10} 0.0")
        
    mps.append("ENDATA")
    
    return {
        "mps": "\n".join(mps),
        "obj_sense": obj_sense,
        "obj_terms": obj_terms,
        "constraints": constraints
    }
