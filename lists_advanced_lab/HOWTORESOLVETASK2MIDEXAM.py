# initial_chest = input().split("|")
#
# command = input()
#
# while command != "Yohoho!":
#     command_arguments = command.split()
#     command = command_arguments[0]
#     if command == "Loot":
#         items = command_arguments[1:]
#         for item in items:
#             if item not in initial_chest:
#                 initial_chest.insert(0, item)
#     elif command == "Drop":
#         index_to_remove = int(command_arguments[1])
#         if index_to_remove < 0 or index_to_remove >= len(initial_chest):
#             command = input()
#             continue
#
#         removed = initial_chest.pop(index_to_remove)
#         initial_chest.append(removed)
#
#     elif command == "Steal":
#         count = int(command_arguments[1])
#         print(", ".join(initial_chest[-count:]))
#         initial_chest = initial_chest[:-count]
#
#     command = input()
#
# if len(initial_chest) == 0:
#     print("Failed treasure hunt.")
# else:
#     sum_treasures = 0
#     for loot in initial_chest:
#         sum_treasures += len(loot)
#     average_sum = sum_treasures / len(initial_chest)
#     print(f"Average treasure gain: {average_sum:.2f} pirate credits.")
#
#




initial_chest = input().split("|")

command = input()
empty_chest = False
while command != "Yohoho!":
    if command.startswith("Loot"):
        command = command.split()
        for index in range(len(command)-1):
            if command[index+1] not in initial_chest:
                initial_chest.insert(0, command[index+1])
    elif command.startswith("Drop"):
        command = command.split()
        index_to_remove = int(command[1])
        if index_to_remove < 0 or index_to_remove >= len(initial_chest):
            command = input()
            continue

        removed = initial_chest.pop(index_to_remove)
        initial_chest.append(removed)
    elif command.startswith("Steal"):
        command = command.split()
        items_to_remove = int(command[1])
        if items_to_remove >= len(initial_chest):
            print(", ".join(initial_chest))
            initial_chest.clear()
            empty_chest = True
            break
        else:
            stolen_items = initial_chest[len(initial_chest)-items_to_remove:len(initial_chest)]
            initial_chest = initial_chest[:len(initial_chest)-items_to_remove]
            print(", ".join(stolen_items))

    command = input()

if empty_chest:
    print("Failed treasure hunt.")
else:
    sum_treasures = 0
    for loot in initial_chest:
        sum_treasures += len(loot)
    average_sum = sum_treasures / len(initial_chest)
    print(f"Average treasure gain: {average_sum:.2f} pirate credits.")