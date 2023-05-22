integer_list = [int(i) for i in input().split()]


def finding_top5(list_integers):
    small_numbers = False
    average_num = sum(list_integers) / len(list_integers)
    bigger_numbers = []
    for i in list_integers:
        if i > average_num:
            bigger_numbers.append(i)
    if len(bigger_numbers) == 0:
        small_numbers = True
    if len(bigger_numbers) > 5:
        bigger_numbers = sorted(bigger_numbers, key=lambda x:-x)
        bigger_numbers = bigger_numbers[:5]
        return bigger_numbers
    if small_numbers:
        return "No"
    bigger_numbers = sorted(bigger_numbers, key=lambda x: -x)
    return bigger_numbers


result = finding_top5(integer_list)
if result == "No":
    print("No")
else:
    result = list(map(str, result))
    print(" ".join(result))
