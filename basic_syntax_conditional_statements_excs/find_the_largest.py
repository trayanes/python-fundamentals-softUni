number = [int(i) for i in input()]

new_list = number
num = ""
for digit in range(len(number)):
    num += str(max(number))
    new_list.remove(max(number))

print(num)



