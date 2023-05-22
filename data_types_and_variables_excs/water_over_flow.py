number_of_lines = int(input())

capacity = 255
empty_tank = 0

for _ in range(number_of_lines):
    litres_water = int(input())
    if empty_tank + litres_water > capacity:
        print("Insufficient capacity!")
        continue
    empty_tank += litres_water
print(empty_tank)