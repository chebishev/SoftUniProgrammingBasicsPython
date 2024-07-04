tree_size = int(input())

for index in range(tree_size + 1):
    start = " " * (tree_size - index) + "*" * index
    end = "*" * index + " " * (tree_size - index)
    print(start + " | " + end)

# test inputs:

# 1

# 2

# 3

# 4
