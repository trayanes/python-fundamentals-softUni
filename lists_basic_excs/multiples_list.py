factor = int(input())
count = int(input())
multiples_list = []
for number in range(factor, factor*count + 1, factor):
    multiples_list.append(number)
print(multiples_list)






# Task:
# Write a program that receives two numbers (factor and count).
# It should create a list with a length of the given count that contains only integer numbers, which are multiples of the given factor.
# The numbers should be only positive, and they should be arranged in ascending order, starting from the value of the factor.