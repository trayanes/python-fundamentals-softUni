def loading_bar_func(number: int):
    percent_num = number // 10
    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{number}% [{percent_num * '%'}{(10-percent_num) * '.'}]")
        print("Still loading...")

num = int(input())
loading_bar_func(num)
