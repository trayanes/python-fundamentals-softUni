def check_even(number):
    return int(number) % 2 == 0


sequence_nums = input().split()
result = list(filter(check_even, sequence_nums))
print(result)