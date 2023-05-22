companions = int(input())
days = int(input())

coins = 0

for day in range(1, days+1):
    if day % 10 == 0:
        companions -= 2
    if day % 15 == 0:
        companions += 5
    coins += 50
    coins -= companions * 2
    if day % 3 == 0:
        coins -= companions * 3
    if day % 5 == 0:
        coins += companions * 20
        if day % 3 == 0:
            coins -= companions * 2
coins_per_comp = coins // companions
print(f"{companions} companions received {coins_per_comp} coins each.")