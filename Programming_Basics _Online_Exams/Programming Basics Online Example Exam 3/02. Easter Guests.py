from math import ceil

easter_bread_price = 4
egg_price = 0.45

guests_count = int(input())
budget = int(input())

easter_bread_count = ceil(guests_count / 3)
total_easter_bread = easter_bread_price * easter_bread_count
total_eggs = guests_count * 2
total_eggs_price = egg_price * total_eggs
total = total_easter_bread + total_eggs_price
difference = budget - total

if difference >= 0:
    print(f"Lyubo bought {easter_bread_count} Easter bread and {total_eggs} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {abs(difference):.2f} lv. more.")

# test inputs:

# 10
# 35

# 9
# 12
