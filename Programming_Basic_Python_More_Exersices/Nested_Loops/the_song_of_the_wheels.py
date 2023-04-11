number = int(input())
counter = 0
password_is_found = False
password_one = 0
password_two = 0
password_three = 0
password_four = 0

for first_number in range(1, 9 + 1):
    for second_number in range(1, 9 + 1):
        for third_number in range(1, 9 + 1):
            for fourth_number in range(1, 9 + 1):
                if ((first_number * second_number) + (third_number * fourth_number)) == number:
                    if first_number >= second_number or \
                            third_number <= fourth_number:
                        continue
                    else:
                        counter += 1
                        print(f"{first_number}{second_number}{third_number}{fourth_number}", end=" ")
                        if counter == 4:
                            password_is_found = True
                            password_one = first_number
                            password_two = second_number
                            password_three = third_number
                            password_four = fourth_number
if password_is_found:
    print()
    print(f"Password: {password_one}{password_two}{password_three}{password_four}")
else:
    print()
    print("No!")

# test input 11
# test input 139
# test input 110
# test input 55
