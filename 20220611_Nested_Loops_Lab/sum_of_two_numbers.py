start = int(input())
end = int(input())
magic_number = int(input())
combinations = 0
magic_number_is_found = False
for first_number in range(start, end + 1):
    for second_number in range(start, end + 1):
        combinations += 1
        if first_number + second_number == magic_number:
            magic_number_is_found = True
            print(f"Combination N:{combinations} ({first_number} + {second_number} = {magic_number})")
            break
    if magic_number_is_found:
        break
if not magic_number_is_found:
    print(f"{combinations} combinations - neither equals {magic_number}")

# test input 1 10 5
# test input 23 24 20
# test input 88 888 1000
# test input 88 888 2000
