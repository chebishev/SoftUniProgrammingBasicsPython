width = int(input())
length = int(input())
height = int(input())
free_volume = width * length * height
command = input()

while command != "Done":
    boxes = int(command)
    free_volume -= boxes
    if free_volume < 0:
        print(f'No more free space! You need {abs(free_volume)} Cubic meters more.')
        break
    else:
        command = input()
        if command == "Done":
            print(f"{free_volume} Cubic meters left.")
            break

# test input 10 10 2 20 20 20 20 122
# test input 10 1 2 4 6 Done
