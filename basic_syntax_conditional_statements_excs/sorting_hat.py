command = input()
voldemort = False

while command != "Welcome!":
    if command == "Voldemort":
        voldemort = True
        break
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")
    command = input()

if voldemort:
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")
