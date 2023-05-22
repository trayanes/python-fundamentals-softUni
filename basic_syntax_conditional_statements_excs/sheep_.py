str_animals = input().split(", ")

list_animals = list(str_animals)
list_animals.reverse()
for index in range(len(list_animals)):
    if list_animals[0] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    elif list_animals[index] == "wolf":
        print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
        break  