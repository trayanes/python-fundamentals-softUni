lines_to_follow = int(input())

counter = 0
balanced_brackets = False

for line in range(1, lines_to_follow+1):
    current_symbol = input()
    if current_symbol == "(":
        counter += 1

    if current_symbol == ")":
        if counter == 1:
            balanced_brackets = True
            counter = 0
        else:
            balanced_brackets = False
            break
if balanced_brackets:
    print("BALANCED")
else:
    print("UNBALANCED")




