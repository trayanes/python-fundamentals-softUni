
def sum_numbers(int1, int2):
    return int1 + int2


def subtract(sums, int3):
    return sums - int3


def add_and_subtract(int1, int2, int3):
    sum_func = sum_numbers(int1, int2)
    result = subtract(sum_func, int3)
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))
