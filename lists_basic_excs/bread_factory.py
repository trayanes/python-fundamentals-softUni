working_days_events = input().split("|")

energy = 100
coins = 100
closed = False

for day_event in working_days_events:
    current_day_event = day_event.split("-")
    event = current_day_event[0]
    number = int(current_day_event[1])
    if event == "rest":
        if number + energy >= 100:
            print("You gained 0 energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            closed = True
            break
if not closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
