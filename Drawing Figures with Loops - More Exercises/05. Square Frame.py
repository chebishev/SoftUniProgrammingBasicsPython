square_size = int(input())

for i in range(1, square_size + 1):
    border_symbol = "+" if i == 1 or i == square_size else "|"
    print(" ".join(border_symbol + "-" * (square_size - 2) + border_symbol))

# test inputs:

# 3

# 4

# 5

# 6
