steps = 0
command = input()

while command != "Going home":
    steps += int(command)
    if steps >= 10000:
        break
    command = input()

if command == "Going home":
    steps += int(input())
diff = abs(steps - 10000)
if steps < 10000:
    print(f'{diff} more steps to reach goal.')
else:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')

# test input 1000 1500 2000 6500
# test input 1500 3000 250 1548 2000 Going home 2000
# test input 1500 300 2500 3000 Going home 200
# test input 125 250 4000 30 2678 4682
