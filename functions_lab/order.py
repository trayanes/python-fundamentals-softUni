def product_calculator(product, quantity):
    total_amount = 0
    if product == "coffee":
        total_amount = quantity * 1.5
    elif product == "coke":
        total_amount = quantity * 1.4
    elif product == "water":
        total_amount = quantity
    elif product == "snacks":
        total_amount = quantity * 2
    return f"{total_amount:.2f}"


prod = input()
quantity_arg = int(input())
print(product_calculator(prod, quantity_arg))