def return_even_odd_sums(string: str):
    odd_sum = 0
    even_sum = 0
    for digit in string:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

number = input()

print(return_even_odd_sums(number))
