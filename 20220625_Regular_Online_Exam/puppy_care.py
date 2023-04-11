food_in_gr = int(input()) * 1000
command = input()
food_eaten = 0

while command != "Adopted":
    eaten_foot_in_gr = int(command)
    food_eaten += eaten_foot_in_gr
    command = input()
diff = abs(food_in_gr - food_eaten)
if food_eaten > food_in_gr:
    print(f"Food is not enough. You need {diff} grams more.")
else:
    print(f"Food is enough! Leftovers: {diff} grams.")

# test input 4 130 345 400 180 230 120 Adopted
# test input 3 1000 1000 1000 Adopted
# test input 2 999 456 999 999 123 456 Adopted