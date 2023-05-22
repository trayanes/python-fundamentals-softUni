command = input()
task_list = [0] * 10

while command != "End":
    command_list = command.split("-")
    importance_num = int(command_list[0])
    task_name = command_list[1]
    task_list.pop(importance_num - 1)
    task_list.insert(importance_num-1, task_name)
    command = input()
result = [x for x in task_list if x != 0]
print(result)