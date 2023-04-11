import sys
command = input()
min_number = sys.maxsize

while command != "Stop":
    temp_number = int(command)
    if temp_number < min_number:
        min_number = temp_number
    command = input()

print(min_number)

# test input 100 99 80 70 Stop
# test input -10 20 -30 Stop
# test input 45 -20 7 99 Stop
# test input 999 Stop
# test input -1 -2 Stop
