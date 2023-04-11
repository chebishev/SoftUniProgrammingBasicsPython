first_range_end = int(input())
second_range_end = int(input())
third_range_end = int(input())

for first_number in range(1, first_range_end + 1):
    for second_number in range(2, second_range_end + 1):
        for third_number in range(1, third_range_end + 1):
            if first_number % 2 == 0 and third_number % 2 == 0:
                if second_number == 2 or \
                        second_number == 3 or \
                        second_number == 5 or \
                        second_number == 7:
                    print(f"{first_number} {second_number} {third_number}")
