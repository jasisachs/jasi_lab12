import sys
import formulas

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) < 2:
        print("Need to provide at least two values and an operator.")
        sys.exit()
    elif len(args) > 3:
        print("Too many arguments provided. You should provide an operator and two values.")
        sys.exit()

    operator = args[0]
    values = [float(val) for val in args[1:]]

    if operator == "add":
        result = formulas.add(values)
    elif operator == "subtract":
        result = formulas.subtract(values)
    elif operator == "multiply":
        result = formulas.multiply(values)
    elif operator == "divide":
        result = formulas.divide(values)
    else:
        print(f"Invalid operator name: {operator}")
        sys.exit()

    if isinstance(result, str):
        print(result)
    else:
        print(f"Result: {result:.2f}")
