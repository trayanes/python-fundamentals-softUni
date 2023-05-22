def is_perfect(number):
    sum_positive_divisors = 0
    for i in range(1, number+1):
        if number % i == 0:
            sum_positive_divisors += i
    if sum_positive_divisors // 2 == number:
        return "We have a perfect number!"
    return "It's not so perfect."


number_argument = int(input())
print(is_perfect(number_argument))
