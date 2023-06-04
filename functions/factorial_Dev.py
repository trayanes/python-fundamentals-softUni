from math import factorial
def find_factorial(num1: int, num2: int):
    '''
    This function calculates the factorial numbers of two integers.
    :return: It returns a result - a number(float) which is the division between the two factorials.
    '''
    result1 = factorial(num1)
    result2 = factorial(num2)
    result = result1 / result2
    print(f"{result:.2f}")

num1 = int(input())
num2 = int(input())
find_factorial(num1, num2)
