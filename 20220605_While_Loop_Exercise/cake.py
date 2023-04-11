length = int(input())
width = int(input())
cake = length * width
command = input()

while command != "STOP":
    pieces = int(command)
    cake -= pieces
    if cake < 0:
        print(f"No more cake left! You need {abs(cake)} pieces more.")
        break
    else:
        command = input()
        if command == "STOP":
            print(f"{cake} pieces are left.")
            break

# test input 10 10 20 20 20 20 21
# test input 10 2 2 4 6 STOP
