film_budget = float(input())
statist_count = int(input())
clothing_per_statist = float(input())
decor = film_budget * 0.10

if statist_count > 150:
    clothing_per_statist *= 0.90

expenses = statist_count * clothing_per_statist + decor

difference = film_budget - expenses
if difference >= 0:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(difference):.2f} leva more.")

# test inputs:

# 20000
# 120
# 55.5

# 15437.62
# 186
# 57.99

# 9587.88
# 222
# 55.68
