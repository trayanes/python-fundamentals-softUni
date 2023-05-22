def loading_bar_func(int_number):
    count_symbol_percent = int_number // 10
    result_loading_bar = f"[{count_symbol_percent * '*'}{(10-count_symbol_percent) * '.'}]"
    return result_loading_bar


integer_number = int(input())
result = loading_bar_func(integer_number)
if 0 <= integer_number <= 99:
    print(f"{integer_number}% {result}")
    print("Still loading...")
elif integer_number == 100:
    print("100% Complete!")
    print(f"{result}")