sequence_nums = [int(i) for i in input().split()]


def find_min(list_ints):
    min_number = min(list_ints)
    return min_number


def find_max(list_ints):
    max_number = max(list_ints)
    return max_number


def sum_numbers(list_ints):
    numbers_sum = sum(list_ints)
    return numbers_sum


print(f"The minimum number is {find_min(sequence_nums)}")
print(f"The maximum number is {find_max(sequence_nums)}")
print(f"The sum number is: {sum_numbers(sequence_nums)}")
