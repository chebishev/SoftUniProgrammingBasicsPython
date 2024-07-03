from math import ceil

easter_bread_count = int(input())
total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0

for bread in range(easter_bread_count):
    used_sugar = int(input())
    total_sugar += used_sugar
    if used_sugar > max_sugar:
        max_sugar = used_sugar
    used_flour = int(input())
    total_flour += used_flour
    if used_flour > max_flour:
        max_flour = used_flour

used_packets_sugar = ceil(total_sugar / 950)
used_packets_flour = ceil(total_flour / 750)

print("Sugar:", used_packets_sugar)
print("Flour:", used_packets_flour)
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")

# test inputs:

# 3
# 400
# 350
# 250
# 300
# 450
# 380

# 4
# 500
# 350
# 560
# 430
# 600
# 345
# 578
# 543
