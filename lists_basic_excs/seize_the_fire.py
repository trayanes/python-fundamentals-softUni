fires = input().split("#")
water_tank = int(input())

total_efford = 0
total_fire_ext = 0

print("Cells:")
for fire in fires:
    valid_cell = False
    current_fire = fire.split(" = ")
    type_of_fire, fire_cell = current_fire[0], int(current_fire[1])
    if type_of_fire == "High" and 81 <= fire_cell <= 125:
        valid_cell = True
    elif type_of_fire == "Medium" and 51 <= fire_cell <= 80:
        valid_cell = True
    elif type_of_fire == "Low" and 1 <= fire_cell <= 50:
        valid_cell = True

    if valid_cell:
        if fire_cell > water_tank:
            continue
        total_efford += fire_cell * 0.25
        total_fire_ext += fire_cell
        water_tank -= fire_cell
        print(f"- {fire_cell}")
print(f"Effort: {total_efford:.2f}")
print(f"Total Fire: {total_fire_ext}")

