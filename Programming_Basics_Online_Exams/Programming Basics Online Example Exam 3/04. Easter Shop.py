initial_eggs_quantity = int(input())
sold_eggs_count = 0
command = input()
while command != "Close":
    if command == "Fill":
        fill_eggs_quantity = int(input())
        initial_eggs_quantity += fill_eggs_quantity
    elif command == "Buy":
        buy_eggs_quantity = int(input())
        if buy_eggs_quantity > initial_eggs_quantity:
            print("Not enough eggs in store!")
            print(f"You can buy only {initial_eggs_quantity}.")
            break
        initial_eggs_quantity -= buy_eggs_quantity
        sold_eggs_count += buy_eggs_quantity

    command = input()
else:
    print("Store is closed!")
    print(f"{sold_eggs_count} eggs sold.")

# test inputs:

# 13
# Buy
# 8
# Fill
# 3
# Buy
# 10

# 20
# Fill
# 30
# Buy
# 15
# Buy
# 20
# Close
