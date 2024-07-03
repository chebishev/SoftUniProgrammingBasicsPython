minutes_per_walking = int(input())
walking_per_day = int(input())
calories_per_day = int(input())

total_walking_minutes = walking_per_day * minutes_per_walking
total_burned_calories = total_walking_minutes * 5
if total_burned_calories >= calories_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.")

# test input 30 3 600
# test input 15 2 500
# test input 40 2 300
