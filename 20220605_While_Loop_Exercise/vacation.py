needed_money = float(input())
actual_money = float(input())
spend_counter = 0
days_counter = 0

while actual_money <= needed_money:
    days_counter += 1
    command = input()
    amount = float(input())
    if command == "spend":
        spend_counter += 1
        if amount > actual_money:
            actual_money = 0
        else:
            actual_money -= amount
    else:
        actual_money += amount
        spend_counter = 0
    if spend_counter == 5:
        break
    if actual_money >= needed_money:
        break

if actual_money >= needed_money:
    print(f'You saved the money for {days_counter} days.')
if spend_counter == 5:
    print("You can't save the money.")
    print(days_counter)

# test input 2000 1000 spend 1200 save 2000
# test input 110 60 spend 10 spend 10 spend 10 spend 10 spend 10
# test input 250 150 spend 50 spend 50 save 100 save 100
