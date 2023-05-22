budget = float(input())
price_1_kg_flour = float(input())
price_1_pack_eggs = price_1_kg_flour * 0.75
price_per_250ml_milk = (price_1_kg_flour * 1.25) / 4
bread_price = price_1_pack_eggs + price_1_kg_flour + price_per_250ml_milk

colored_eggs = 0
bread_counter = 0

while budget >= bread_price:
    bread_counter += 1
    colored_eggs += 3
    if bread_counter % 3 == 0:
        colored_eggs -= bread_counter - 2
    budget -= bread_price
print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


