from math import ceil

sunglasses_size = int(input())
max_size = 5 * sunglasses_size
middle_row = ceil(sunglasses_size / 2) - 1

for index in range(sunglasses_size):
    stars = sunglasses_size * 2
    blanks = max_size - stars * 2
    if index == 0 or index == sunglasses_size - 1:
        print("*" * stars + " " * blanks + "*" * stars)
    else:
        if index == middle_row:
            middle = "|" * blanks
        else:
            middle = " " * blanks
        print("*" + ("/" * (stars - 2)) + "*" + middle + "*" + ("/" * (stars - 2)) + "*")

# test inputs:

# 3

# 4

# 5
