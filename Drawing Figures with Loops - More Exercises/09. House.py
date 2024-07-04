house_size = int(input())
roof_size = (house_size + 1) // 2
start_stars = 2 if house_size % 2 == 0 else 1

for row in range(roof_size):
    dashes = (house_size - start_stars) // 2
    print("-" * dashes + start_stars * "*" + "-" * dashes)
    start_stars += 2


for row in range(house_size // 2):
    stars = house_size - 2
    print("|" + "*" * stars + "|")

# test inputs:

# 2

# 3

# 4

# 5

# 6
