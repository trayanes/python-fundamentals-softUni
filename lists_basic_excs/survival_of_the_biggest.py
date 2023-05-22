list_of_ints = [int(x) for x in input().split()]
count_nums_to_remove = int(input())

for _ in range(count_nums_to_remove):
    list_of_ints.remove(min(list_of_ints))
copy_list = list(map(str, list_of_ints))
print(", ".join(copy_list))



# Task:
# Write a program that receives a list of integer numbers (separated by a single space) and a number n. The number n represents the count of numbers to remove from the list.
# You should remove the smallest ones, and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".