groceries_list = input().split("!")


command = input()

while command != "Go Shopping!":
    command_args = command.split()
    command = command_args[0]
    if command == "Urgent":
        if command_args[1] in groceries_list:
            command = input()
            continue
        groceries_list.insert(0, command_args[1])

    elif command == "Unnecessary":
        if command_args[1] not in groceries_list:
            command = input()
            continue
        groceries_list.remove(command_args[1])

    elif command == "Correct":
        if command_args[1] not in groceries_list:
            command = input()
            continue
        for index in range(len(groceries_list)):
            if groceries_list[index] == command_args[1]:
                groceries_list[index] = command_args[2]
    elif command == "Rearrange":
        if command_args[1] not in groceries_list:
            command = input()
            continue
        groceries_list.remove(command_args[1])
        groceries_list.append(command_args[1])
    command = input()
print(", ".join(groceries_list))