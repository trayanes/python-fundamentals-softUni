
command = input()
coffee_counter = 0

while command != "END":
    if command == command.lower():
        if command == "coding" or command == "dog" or command == "cat" or command == "movie":
            coffee_counter += 1
    elif command == command.upper():
        if command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
            coffee_counter += 2
    command = input()

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)







command = ''

coffees_needed = 0
while command.lower() != "end":
    command = input()
    if command.lower() == 'coding' or command.lower() == 'dog' \
            or command.lower() == 'cat' or command.lower() == 'movie':
        if command.islower():
            coffees_needed += 1
        else: #elif command.isupper():
            coffees_needed += 2
if coffees_needed > 5:
    print("You need extra sleep")
else:
    print(coffees_needed)