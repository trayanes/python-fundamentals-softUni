count_lines = int(input())

even = []
odd = []
negative = []
positive = []


for line in range(count_lines):
    current_int = int(input())
    if current_int >= 0:
        positive.append(current_int)
    else:
        negative.append(current_int)
    if current_int % 2 == 0:
        even.append(current_int)
    else:
        odd.append(current_int)
condition = input()
if condition == "even":
    print(even)
elif condition == "odd":
    print(odd)
elif condition == "positive":
    print(positive)
elif condition == "negative":
    print(negative)


# Task:
# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.