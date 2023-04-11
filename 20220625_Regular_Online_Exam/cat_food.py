cats_count = int(input())
grams_counter = 0
group_one = 0
group_two = 0
group_three = 0

for cat in range(cats_count):
    food_in_gr = float(input())
    grams_counter += food_in_gr
    if 100 <= food_in_gr < 200:
        group_one += 1
    elif 200 <= food_in_gr < 300:
        group_two += 1
    else:
        group_three += 1

kilograms = grams_counter / 1000
price = kilograms * 12.45

print(f"Group 1: {group_one} cats.")
print(f"Group 2: {group_two} cats.")
print(f"Group 3: {group_three} cats.")
print(f"Price for food per day: {price:.2f} lv.")

# test input 6 102 236 123 399 342 222
# test input 10 256 348 198 322 186 294 321 100 200 300
# test input 7 100 200 342 300 234 123 212
