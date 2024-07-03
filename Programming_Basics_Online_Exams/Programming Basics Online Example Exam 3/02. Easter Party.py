guests_count = int(input())
price_for_person = float(input())
budget = float(input())

if 10 <= guests_count <= 15:
    price_for_person *= 0.85
elif 15 < guests_count <= 20:
    price_for_person *= 0.80
elif guests_count > 20:
    price_for_person *= 0.75

cake_price = budget * 0.10

total = guests_count * price_for_person
total += cake_price

difference = budget - total

if difference >= 0:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {abs(difference):.2f} leva needed.")

# test inputs:

# 18
# 30
# 450

# 8
# 25
# 340

# 24
# 35
# 550


