budget = int(input())

total_sum = 0

while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    price = int(command)
    if total_sum + price > budget:
        print("You went in overdraft!")
        break
    total_sum += price
