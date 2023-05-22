count_integers = int(input())

positive_int_list = []
negative_int_list = []
for num in range(count_integers):
    current_num = int(input())
    if current_num > 0:
        positive_int_list.append(current_num)
    else:
        negative_int_list.append(current_num)
print(positive_int_list)
print(negative_int_list)
print(f"Count of positives: {len(positive_int_list)}")
print(f"Sum of negatives: {sum(negative_int_list)}")





# Task:
# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"