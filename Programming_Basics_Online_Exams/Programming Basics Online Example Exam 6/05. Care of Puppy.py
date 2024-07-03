food_in_grams = int(input()) * 1000
food_eaten_in_grams = 0

command = input()
while command != "Adopted":
    food_eaten_in_grams += int(command)
    command = input()

difference = abs(food_in_grams - food_eaten_in_grams)
if food_eaten_in_grams > food_in_grams:
    print(f"Food is not enough. You need {difference} grams more.")
else:
    print(f"Food is enough! Leftovers: {difference} grams.")

# test inputs:
# 4
# 130
# 345
# 400
# 180
# 230
# 120
# Adopted

# 3
# 1000
# 1000
# 1000
# Adopted

# 2
# 999
# 456
# 999
# 999
# 123
# 456
# Adopted
