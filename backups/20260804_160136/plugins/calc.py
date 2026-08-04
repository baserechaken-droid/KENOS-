import math

NAME = "calc"
DESCRIPTION = "Evaluate mathematical expressions"

SAFE_FUNCTIONS = {
    "sqrt": math.sqrt,
    "pow": pow,
    "abs": abs,
    "round": round,
    "pi": math.pi,
    "e": math.e,
}

def run(args):
    if not args:
        print("Usage: calc <expression>")
        return

    expression = " ".join(args)

    try:
        result = eval(expression, {"__builtins__": {}}, SAFE_FUNCTIONS)
        print(result)
    except Exception as e:
        print("Calculation error:", e)
