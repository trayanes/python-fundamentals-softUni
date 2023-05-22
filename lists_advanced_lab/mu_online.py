killed = False
room_counter = 0
dungeons_rooms = input().split("|")

health = 100
bitcoins = 0

for string in dungeons_rooms:
    room_counter += 1
    command_arguments = string.split()
    command = command_arguments[0]
    if command == "potion":
        amount_healed = int(command_arguments[1])
        if health + amount_healed >= 100:
            if health == 100:
                print("You healed for 0 hp.")
            else:
                diff = (health + amount_healed) - 100
                amount_healed -= diff
                health += amount_healed
                print(f"You healed for {amount_healed} hp.")
        else:
            health += amount_healed
            print(f"You healed for {amount_healed} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        amount_found = command_arguments[1]
        bitcoins += int(amount_found)
        print(f"You found {amount_found} bitcoins.")
    else:
        monster = command
        monster_attack = int(command_arguments[1])
        health -= monster_attack

        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_counter}")
            killed = True
            break

if not killed:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")