def sum_numbers(int1: int, int2: int) -> int:
    return int1 + int2


def add_and_subtract(int1:int, int2: int, int3:int) -> int:
    return sum_numbers(int1, int2) - int3

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))