n = int(input())
string_is_pure = True
for i in range(n):
    string = input()
    for char in range(len(string)):
        # print(f"{char} : {string[char]}")
        if string[char] == "." or string[char] == "," or string[char] == "_":
            string_is_pure = False
            break
    if string_is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")