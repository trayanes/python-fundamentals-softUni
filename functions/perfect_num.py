def check_if_perfect(number: int):
    sum_divisors = 0
    for i in range(1, number+1):
        if number % i == 0:
            sum_divisors += i
    if sum_divisors / 2 == number:
        return f"We have a perfect number!"
    else:
        return f"It's not so perfect."


num = int(input())
print(check_if_perfect(num))
