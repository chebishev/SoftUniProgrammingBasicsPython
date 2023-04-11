numbers_count = int(input())
total = 0

for numbers in range(numbers_count):
    temp_number = int(input())
    total += temp_number
average = total / numbers_count
print(f'{average:.2f}')

# test input 4 3 2 4 2
# test input 2 6 4
# test input 3 82 43 22
# test input 4 95 23 76 23
