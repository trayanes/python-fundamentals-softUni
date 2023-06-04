def find_smallest(int1: int, int2: int, int3: int) -> int:
    return min(int1, int2, int3)

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(find_smallest(num1, num2, num3))
