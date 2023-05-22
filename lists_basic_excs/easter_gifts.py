name_of_the_gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    command = command.split()
    if "OutOfStock" in command:
        for index_gift in range(len(name_of_the_gifts)):
            if name_of_the_gifts[index_gift] == command[1]:
                name_of_the_gifts[index_gift] = "None"
    elif "Required" in command:
        if len(name_of_the_gifts) >= int(command[2]) >= 0:
            name_of_the_gifts[int(command[2])] = command[1]
    elif "JustInCase" in command:
        name_of_the_gifts[-1] = command[1]

while "None" in name_of_the_gifts:
    name_of_the_gifts.remove("None")
print(" ".join(name_of_the_gifts))