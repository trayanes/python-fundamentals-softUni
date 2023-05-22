array_list = [int(i) for i in input().split()]

command = input()

while command != "end":
    command_argument = command.split()
    command = command_argument[0]

    if command == "decrease":
        array_list = [int(j-1) for j in array_list]
        command = input()
        continue
    index1 = int(command_argument[1])
    index2 = int(command_argument[2])
    if command == "swap":
        array_list[index1], array_list[index2] = array_list[index2], array_list[index1]
    elif command == "multiply":
        array_list[index1] *= array_list[index2]

    command = input()
array_list = list(map(str, array_list))
print(", ".join(array_list))