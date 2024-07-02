eggs_size = input()
eggs_color = input()
eggs_peels_count = int(input())

possible_colors = ["Red", "Green", "Yellow"]
color_index = possible_colors.index(eggs_color)
eggs_dictionary = {
    "Large": [16, 12, 9],
    "Medium": [13, 9, 7],
    "Small": [9, 8, 5]
}
profit = eggs_dictionary[eggs_size][color_index] * eggs_peels_count
manufacturing_expenses = profit * 0.35
total = profit - manufacturing_expenses

print(f"{total:.2f} leva.")

# test inputs:

# Large
# Red
# 7

# Medium
# Green
# 5

# Small
# Yellow
# 3
