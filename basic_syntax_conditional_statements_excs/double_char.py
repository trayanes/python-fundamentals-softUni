command = input()


while command != "End":
    if command != "SoftUni":
        new_string = ""
        for index in range(len(command)):
            new_string += 2 * command[index]
        print(new_string)
    command = input()