quantity_food = float(input()) * 1000
quantity_hay = float(input()) * 1000
quantity_cover = float(input()) * 1000
pigs_weight = float(input()) * 1000


counter_days = 1

while counter_days != 31:
    quantity_food -= 300
    if counter_days % 2 == 0:
        quantity_hay -= quantity_food * 0.05
    if counter_days % 3 == 0:
        quantity_cover -= pigs_weight / 3
    if quantity_food <= 0 or quantity_cover <= 0 or quantity_hay <= 0:
        break
    counter_days += 1

if counter_days == 31:
    print(f"Everything is fine! Puppy is happy! Food: {quantity_food / 1000:.2f}, Hay: {quantity_hay / 1000:.2f}, Cover: {quantity_cover / 1000:.2f}.")
else:
    print(f"Merry must go to the pet store!")