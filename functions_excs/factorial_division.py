def factorial(number):
    fact = 1
    if number > 0:
        for i in range(1, number+1):
            fact = fact * i
        return fact


num_arg = int(input())
num2_arg = int(input())
result = factorial(num_arg) / factorial(num2_arg)
print(f"{result:.2f}")


