string1 = input()
string2 = input()

new_word = ""

for index in range(len(string1)):
    if string1[index] == string2[index]:
        continue
    new_word = string2[:index+1] + string1[index+1:]
    print(new_word)
