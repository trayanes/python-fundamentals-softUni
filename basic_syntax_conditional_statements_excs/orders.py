number_of_orders = int(input())
total_sum_orders = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        current_day_sum = (price_per_capsule * capsules_per_day) * days
        total_sum_orders += current_day_sum
        print(f"The price for the coffee is: ${current_day_sum:.2f}")
print(f"Total: ${total_sum_orders:.2f}")