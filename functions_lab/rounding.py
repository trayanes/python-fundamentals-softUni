numbers_given = [float(i) for i in input().split()]
result_list = []
for num in numbers_given:
    result_list.append(round((num)))
print(result_list)