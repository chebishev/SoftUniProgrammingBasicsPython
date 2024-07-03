destination = input()
dates = input()
nights = int(input())

possible_dates = ["21-23", "24-27", "28-31"]
date_index = possible_dates.index(dates)

destinations = {
    "France": [30, 35, 40],
    "Italy": [28, 32, 39],
    "Germany": [32, 37, 43]
}
total_cost = destinations[destination][date_index] * nights

print(f"Easter trip to {destination} : {total_cost:.2f} leva.")

# test inputs:

# Germany
# 24-27
# 5

# Italy
# 21-23
# 7

# France
# 28-31
# 8
