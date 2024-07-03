fruit = input()
item_size = input()
ordered_items = int(input())
price = 0

if item_size == "small":
    ordered_items *= 2
    if fruit == "Watermelon":
        price = ordered_items * 56
    elif fruit == "Mango":
        price = ordered_items * 36.66
    elif fruit == "Pineapple":
        price = ordered_items * 42.10
    else:
        price = ordered_items * 20
else:
    ordered_items *= 5
    if fruit == "Watermelon":
        price = ordered_items * 28.70
    elif fruit == "Mango":
        price = ordered_items * 19.60
    elif fruit == "Pineapple":
        price = ordered_items * 24.80
    else:
        price = ordered_items * 15.20
if 400 <= price <= 1000:
    price *= 0.85
elif price > 1000:
    price *= 0.50
print(f"{price:.2f} lv.")

# test input Watermelon big 4
# test input Pineapple small 1
# test input Raspberry small 50
# test input Mango big 8
