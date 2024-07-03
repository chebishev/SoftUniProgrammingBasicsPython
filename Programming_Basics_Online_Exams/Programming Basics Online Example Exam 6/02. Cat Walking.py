walk_in_minutes = int(input())
walks_count_per_day = int(input())
calories_taken_per_day = int(input())

burned_calories = walks_count_per_day * (walk_in_minutes * 5)
calories_checkpoint = calories_taken_per_day / 2
if burned_calories >= calories_checkpoint:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")

# test inputs:
# 30
# 3
# 600

# 15
# 2
# 500
