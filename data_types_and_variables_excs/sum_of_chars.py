letters_to_read = int(input())
total_sum = 0
for letter in range(letters_to_read):
    current_letter = input()
    total_sum += ord(current_letter)
print(f"The sum equals: {total_sum}")