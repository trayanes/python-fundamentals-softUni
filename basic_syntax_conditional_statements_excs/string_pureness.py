# number_of_strings = int(input())
# bad_char1 = "_"
# bad_char2 = ","
# bad_char3 = "."
# for _ in range(number_of_strings):
#     string = input()
#     if bad_char1 in string or bad_char2 in string or bad_char3 in string:
#         print(f"{string} is not pure!")
#     else:
#         print(f"{string} is pure.")

number_of_strings = int(input())


for _ in range(number_of_strings):
    string = input()
    for index in range(len(string)):
        if string[index] == "," or string[index] == "_" or string[index] == ".":
            print(f"{string} is not pure!")
            break
    else:
        print(print(f"{string} is pure."))



