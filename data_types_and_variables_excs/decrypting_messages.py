key = int(input())
number_of_lines = int(input())

message = ""

for _ in range(1, number_of_lines+1):
    current_letter = ord(input())
    ascii_value_to_add = current_letter + key
    message += chr(ascii_value_to_add)
print(message)