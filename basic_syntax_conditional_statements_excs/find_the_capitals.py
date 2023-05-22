string = input()

string_indx = []

for index in range(len(string)):
    if string[index].isupper():
        string_indx.append(index)
print(string_indx)