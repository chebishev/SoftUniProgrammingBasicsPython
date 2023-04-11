operation = input()
while operation != "stop":
    first_number = float(input())
    second_number = float(input())
    total = 0
    if operation == "+":
        total = first_number + second_number
        print(f"{first_number} + {second_number} = {total}")
    elif operation == "-":
        total = first_number - second_number
        print(f"{first_number} - {second_number} = {total}")
    elif operation == "*":
        total = first_number * second_number
        print(f"{first_number} * {second_number} = {total}")
    elif operation == "/":
        if second_number != 0:
            total = first_number / second_number
            print(f"{first_number} / {second_number} = {total}")
        else:
            print("invalid operation!")
    operation = input()