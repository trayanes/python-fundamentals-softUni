initial_energy = int(input())

command = input()
battles_won = 0
battle_lost = False
while command != "End of battle":
    if initial_energy == 0:
        battle_lost = True
        break
    distance = int(command)
    if distance <= initial_energy:
        initial_energy -= distance
        battles_won += 1
    else:
        battle_lost = True
        break
    if battles_won % 3 == 0:
        initial_energy += battles_won

    command = input()

if battle_lost:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
else:
    print(f"Won battles: {battles_won}. Energy left: {initial_energy}")