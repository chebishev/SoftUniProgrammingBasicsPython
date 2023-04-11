from math import ceil
average_speed = float(input())
liters_per_hundred_km = float(input())

all_distance = 384400 * 2
hours = ceil(all_distance / average_speed) + 3
fuel = (liters_per_hundred_km * all_distance) / 100
print(hours)
print(int(fuel))

# test input 10000 5
# test input 5000 7
# test input 15000 4
