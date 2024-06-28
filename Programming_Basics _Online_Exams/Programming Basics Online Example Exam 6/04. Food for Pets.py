days = int(input())
total_food_quantity = float(input())
food_eaten_quantity = 0
dog_food_eaten_quantity = 0
cat_food_eaten_quantity = 0
eaten_biscuits_in_grams = 0

for day in range(1, days + 1):
    dog_food_eaten = int(input())
    cat_food_eaten = int(input())
    food_eaten_quantity += dog_food_eaten + cat_food_eaten
    dog_food_eaten_quantity += dog_food_eaten
    cat_food_eaten_quantity += cat_food_eaten

    if day % 3 == 0:
        eaten_biscuits_in_grams += (dog_food_eaten * 0.10) + (cat_food_eaten * 0.10)

print(f"Total eaten biscuits: {round(eaten_biscuits_in_grams)}gr.")

food_eaten_percentage = food_eaten_quantity / total_food_quantity
print(f"{food_eaten_percentage * 100:.2f}% of the food has been eaten.")

total_food_eaten = total_food_quantity * food_eaten_percentage
dog_food_eaten_percentage = dog_food_eaten_quantity / total_food_eaten * 100
cat_food_eaten_percentage = cat_food_eaten_quantity / total_food_eaten * 100
print(f"{dog_food_eaten_percentage:.2f}% eaten from the dog.")
print(f"{cat_food_eaten_percentage:.2f}% eaten from the cat.")

# test inputs:
# 3
# 1000
# 300
# 20
# 100
# 30
# 110
# 40

# 3
# 500
# 100
# 30
# 110
# 25
# 120
# 35
