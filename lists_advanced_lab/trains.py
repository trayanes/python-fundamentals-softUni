number_wagons = int(input())
wagons_list = [0] * number_wagons

command = input()

while command != "End":
    if command.startswith("add"):
        command = command.split()
        people_to_add = int(command[1])
        wagons_list[-1] += people_to_add
    elif command.startswith("insert"):
        command = command.split()
        index = int(command[1])
        people_to_add = command[2]
        wagons_list[index] += int(people_to_add)
    elif command.startswith("leave"):
        command = command.split()
        index = int(command[1])
        people_to_add = command[2]
        wagons_list[index] -= int(people_to_add)
    command = input()
print(wagons_list)