target_list = [int(i) for i in input().split()]

command = input()
invalid_target = False
shot_targets = 0

while command != "End":
    index = int(command)
    if index > len(target_list)-1:
        invalid_target = True
        command = input()
        continue

    if target_list[index] == -1:
        command = input()
        continue
    old_target_value = target_list.pop(index)
    target_list.insert(index, -1)
    shot_targets += 1
    for i in range(len(target_list)):
        if target_list[i] == -1:
            continue

        elif target_list[i] > old_target_value:
            target_list[i] -= old_target_value
        else:
            target_list[i] += old_target_value
    command = input()
target_list_str = list(map(str, target_list))
result = " ".join(target_list_str)
print(f"Shot targets: {shot_targets} -> {result}")
