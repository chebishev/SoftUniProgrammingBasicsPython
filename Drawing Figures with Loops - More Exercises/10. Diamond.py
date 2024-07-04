diamond_size = int(input())
start_stars = 2 if diamond_size % 2 == 0 else 1
range_limit = diamond_size // 2 + 1 if diamond_size % 2 != 0 else diamond_size // 2
dashes = (diamond_size - start_stars) // 2
up_dashes = dashes

middles_dashes = 1 if diamond_size % 2 == 0 else 0
for index in range(range_limit):
    if index == 0:
        print("-" * dashes + start_stars * "*" + "-" * dashes)
    else:
        print("-" * up_dashes + "*" + "-" * (middles_dashes + index) + "*" + "-" * up_dashes)
        middles_dashes += 1
    up_dashes -= 1

middles_dashes -= 2
up_dashes += 2
for index in range(range_limit - 2, -1, -1):
    if index == 0:
        print("-" * dashes + start_stars * "*" + "-" * dashes)
    else:
        print("-" * up_dashes + "*" + "-" * (middles_dashes + index) + "*" + "-" * up_dashes)
        middles_dashes -= 1
    up_dashes += 1
