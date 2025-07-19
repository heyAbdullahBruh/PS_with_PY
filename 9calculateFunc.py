#Problem-9-->Build a function calculate(a, b, operator)

def calculate(a, b, operator="+"):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    elif operator == "%":
        if b == 0:
            return "Error: Modulo by zero"
        return a % b
    elif operator == "^":
        return a ** b
    else:
        return "Error: Invalid operator"

print(calculate(10, 5, "+"))  # 15
print(calculate(10, 0, "/"))  # Error: Division by zero
print(calculate(2, 3, "^"))   # 8
print(calculate(4, 2, "x"))   # Error: Invalid operator


