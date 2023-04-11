result = int(input())
combinations = 0

for first_number in range (result+1):
    for second_number in range(result+1):
        for third_number in range(result+1):
            if first_number + second_number + third_number == result:
                combinations += 1

print(combinations)

# test input 25
# test input 20
# test input 5
