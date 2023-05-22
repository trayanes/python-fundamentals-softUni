def find_smallest_int(int1, int2, int3):
    smallest_num = min(int1, int2, int3)
    return smallest_num


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(find_smallest_int(num1, num2, num3))

