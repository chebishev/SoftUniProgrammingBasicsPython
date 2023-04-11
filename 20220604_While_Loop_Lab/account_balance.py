account_balance = 0

while True:
    command = input()
    if command == "NoMoreMoney":
        break
    else:
        ammount = float(command)
        if ammount < 0:
            print("Invalid operation!")
            break
        else:
            account_balance += ammount
            print(f"Increase: {ammount:.2f}")
    
print(f"Total: {account_balance:.2f}")

# test input 5.51 69.42 100 NoMoreMoney
# test input 120 45.55 -150
