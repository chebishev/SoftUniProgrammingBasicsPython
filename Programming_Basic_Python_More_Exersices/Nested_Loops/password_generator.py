first_end_range = int(input())
second_end_range = int(input())
letters_range = second_end_range + 97

for first_number in range(1, first_end_range + 1):
    for second_number in range(1, first_end_range + 1):
        for first_letter in range(97, letters_range):
            for second_letter in range(97, letters_range):
                for last_number in range(1, first_end_range + 1):
                    if last_number > first_number and \
                            last_number > second_number:
                        print(f"{first_number}{second_number}{chr(first_letter)}{chr(second_letter)}{last_number}", end=" ")

# test input 2 4
# test input 3 1
# test input 3 2
# test input 4 2
