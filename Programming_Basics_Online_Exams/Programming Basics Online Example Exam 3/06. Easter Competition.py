easter_breads_count = int(input())
max_points = 0
max_chef = ""

for bread in range(easter_breads_count):
    current_points = 0
    current_chef = input()
    points = input()
    while points != "Stop":
        current_points += int(points)
        points = input()

    print(f"{current_chef} has {current_points} points.")

    if current_points > max_points:
        max_points = current_points
        max_chef = current_chef
        print(f"{current_chef} is the new number 1!")

print(f"{max_chef} won competition with {max_points} points!")

# test inputs:

# 3
# Chef Manchev
# 10
# 10
# 10
# 10
# Stop
# Natalie
# 8
# 2
# 9
# Stop
# George
# 9
# 2
# 4
# 2
# Stop

# 2
# Chef Angelov
# 9
# 9
# 9
# Stop
# Chef Rowe
# 10
# 10
# 10
# 10
# Stop
