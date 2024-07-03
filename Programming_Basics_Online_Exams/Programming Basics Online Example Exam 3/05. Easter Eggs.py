eggs_quantity = int(input())
eggs_colors = {
    "red": 0,
    "orange": 0,
    "blue": 0,
    "green": 0,
}
max_eggs = 0
max_color = ""
for egg in range(eggs_quantity):
    current_color = input()
    eggs_colors[current_color] += 1
    if eggs_colors[current_color] > max_eggs:
        max_eggs = eggs_colors[current_color]
        max_color = current_color

for color, count in eggs_colors.items():
    print(f"{color.title()} eggs: {count}")

print(f"Max eggs: {max_eggs} -> {max_color}")

# test inputs:

# 7
# orange
# blue
# green
# green
# blue
# red
# green

# 4
# blue
# red
# blue
# orange
