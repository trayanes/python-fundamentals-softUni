string = input()
words_list = ["Sand", "Water", "Fish", "Sun"]
string_list = string.lower()
counter = 0
for word in words_list:
    a = string_list.count(word.lower())
    counter += a
print(counter)

