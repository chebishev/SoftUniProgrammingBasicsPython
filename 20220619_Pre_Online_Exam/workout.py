from math import ceil
days = int(input())
km_per_day = float(input())
total_km = km_per_day

for day in range(days):
    temp_km = int(input())
    km_per_day *= ((temp_km / 100) + 1)
    total_km += km_per_day

diff = abs(1000 - total_km)
if total_km >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:

    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")
