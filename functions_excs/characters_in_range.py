def chars_in_range(char1: str, char2: str):
    found_symbols = []
    for i in range(ord(char1)+1, ord(char2)):
        found_symbols.append(chr(i))
    return found_symbols


char1_arg = input()
char2_arg = input()
result = chars_in_range(char1_arg, char2_arg)
print(" ".join(result))
