def sum_digits_odd_and_even(number: str):
    sum_odd = 0
    sum_even = 0
    for digit_str in number:
        digit_int = int(digit_str)
        if digit_int % 2 != 0:
            sum_odd += digit_int
        else:
            sum_even += digit_int
    return sum_odd, sum_even


number_arg = input()
result = sum_digits_odd_and_even(number_arg)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")


