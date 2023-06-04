# def factorial(number):
#     fact = number
#     for i in range(1, number):
#         fact *= i
#     return fact
#
#
# print(factorial(5))


def find_tribbo(number: int):
    n1 = 0
    n2 = 1
    n3 = 1
    tribbo = 0
    if number <= 0:
        return 0
    elif number == 1:
        return number
    else:
        tribbo_seq = [n2, n3]
        for i in range(2, number):
            tribbo = n1 + n2 + n3
            tribbo_seq.append(tribbo)
            n1 = n2
            n2 = n3
            n3 = tribbo
        result = " ".join(list(map(str, tribbo_seq)))
        return result


num_input = int(input())
print(find_tribbo(num_input))


