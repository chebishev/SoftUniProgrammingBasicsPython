days = int(input())
food_quantity = float(input())
food_counter = 0
total_biscuits = 0
dog_counter = 0
cat_counter = 0

for day in range(1, days + 1):
    dog_food_eaten = int(input())
    cat_foot_eaten = int(input())
    dog_counter += dog_food_eaten
    cat_counter += cat_foot_eaten
    total_day_eaten = dog_food_eaten + cat_foot_eaten
    food_counter += total_day_eaten
    if day % 3 == 0:
        total_biscuits += total_day_eaten * 0.10
food_percent = food_counter / food_quantity * 100
dog_percent = dog_counter / food_counter * 100
cat_percent = cat_counter / food_counter * 100
print(f"Total eaten biscuits: {total_biscuits:.0f}gr.")
print(f"{food_percent:.2f}% of the food has been eaten.")
print(f"{dog_percent:.2f}% eaten from the dog.")
print(f"{cat_percent:.2f}% eaten from the cat.")

# test input 3 1000 300 20 100 30 110 40
# test input 3 500 100 30 110 25 120 35
