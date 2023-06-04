def chars_in_range(string1: str, string2: str) -> str:
    result = [chr(i) for i in range(ord(string1)+1, ord(string2))]
    result = " ".join(result)
    return result


char1 = input()
char2 = input()

print(chars_in_range(char1, char2))