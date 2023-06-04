def min_max_sum_func(list):
    min_list = min(list)
    max_list = max(list)
    sum_list = sum(list)
    print(f"The minimum number is {min_list}")
    print(f"The maximum number is {max_list}")
    print(f"The sum number is: {sum_list}")

user_input = list(map(int, input().split()))

min_max_sum_func(user_input)

