items_to_buy = input().split("|")
budget = int(input())

profit = 0
list_with_valid_items_price = []

for item in items_to_buy:
    valid_item = False
    current_item = item.split("->")
    item_type, price = current_item[0], float(current_item[1])
    if item_type == "Clothes" and price <= 50:
        valid_item = True
    elif item_type == "Shoes" and price <= 35:
        valid_item = True
    elif item_type == "Accessories" and price <= 20.5:
        valid_item = True

    if valid_item:
        if budget >= price:
            budget -= price
            list_with_valid_items_price.append(price)

for item_index in range(len(list_with_valid_items_price)):
    profit += list_with_valid_items_price[item_index] * 0.4
    list_with_valid_items_price[item_index] = list_with_valid_items_price[item_index] * 1.4
for _ in range(len(list_with_valid_items_price)):
    print(f"{list_with_valid_items_price[_]:.2f}", end=' ')
print()
print(f"Profit: {profit:.2f}")
if sum(list_with_valid_items_price) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
