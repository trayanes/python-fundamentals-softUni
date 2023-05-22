quantity = int(input())
days = int(input())

total_cost = 0
total_spirit = 0

for day in range(1, days+1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += quantity * 2
        total_spirit += 5
    if day % 3 == 0:
        total_cost += quantity * 8
        total_spirit += 10 + 3
    if day % 5 == 0:
        total_cost += quantity * 15
        total_spirit += 17
    if day % 3 == 0 and day % 5 == 0:
        total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += 5 + 3 + 15
if days == 10:
    total_spirit -= 30
print(f"Total cost: {total_cost:.0f}")
print(f"Total spirit: {total_spirit}")

