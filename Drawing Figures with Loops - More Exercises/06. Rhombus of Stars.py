rombus_size = int(input())

for i in range(1, rombus_size + 1):
    print(" " * (rombus_size - i) + " ".join("*" * i))

for i in range(rombus_size - 1, 0, -1):
    print(" " * (rombus_size - i) + " ".join("*" * i))

# 1

# 2

# 3

# 4
