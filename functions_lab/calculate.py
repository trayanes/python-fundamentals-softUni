def calculate(operator, num1, num2):
    result = 0
    if operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = num1 // num2
    elif operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2
    return result


op = input()
num1_arg = int(input())
num2_arg = int(input())
print(calculate(op, num1_arg, num2_arg))
