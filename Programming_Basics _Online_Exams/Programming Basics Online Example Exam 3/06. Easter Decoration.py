clients_count = int(input())
total_paid_from_clients = 0

products = {
    "basket": 1.50,
    "wreath": 3.80,
    "chocolate bunny": 7.00
}

for client in range(clients_count):
    command = input()
    bought_items = 0
    current_bill = 0
    while command != "Finish":
        bought_items += 1
        current_price = products[command]
        current_bill += current_price
        command = input()

    if bought_items % 2 == 0:
        current_bill *= 0.8

    total_paid_from_clients += current_bill

    print(f"You purchased {bought_items} items for {current_bill:.2f} leva.")

average_bill_per_client = total_paid_from_clients / clients_count
print(f"Average bill per client is: {average_bill_per_client:.2f} leva.")

# test inputs:

# 2
# basket
# wreath
# chocolate bunny
# Finish
# wreath
# chocolate bunny
# Finish

# 1
# basket
# wreath
# chocolate bunny
# wreath
# basket
# chocolate bunny
# Finish
