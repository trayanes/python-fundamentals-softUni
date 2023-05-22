number_of_snowballs = int(input())

max_snowball = 0
max_snowball_value = ""

for snowball in range(number_of_snowballs):
    weight = int(input())
    time_to_target = int(input())
    quality = int(input())
    value = (weight // time_to_target) ** quality
    if value > max_snowball:
        max_snowball = value
        max_snowball_value = f"{weight} : {time_to_target} = {value} ({quality})"
print(max_snowball_value)