count_lines = int(input())
word = input()

words_list = []
filtered_words_list = []


for line in range(count_lines):
    current_string = input()
    words_list.append(current_string)
    if word in current_string:
        filtered_words_list.append(current_string)
print(words_list)
print(filtered_words_list)


# Task:
# On the first line, you will receive a number n.
# On the second line, you will receive a word. On the following n lines, you will be given some strings.
# You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.