first_pair_start_range = int(input())
second_pair_start_range = int(input())
first_pair_end_range = first_pair_start_range + int(input())
second_pair_end_range = second_pair_start_range + int(input())
first_is_prime = False
second_is_prime = False

for first_pair in range(first_pair_start_range, first_pair_end_range + 1):
    for second_pair in range(second_pair_start_range, second_pair_end_range + 1):
        first_current_number = first_pair
        second_current_number = second_pair
        if first_current_number > 1:
            for first_number in range(2, first_current_number // 2):
                if(first_current_number % first_number) == 0:
                    first_is_prime = False
                    break
                else:
                    first_is_prime = True
                    first_prime_number = first_current_number
        else:
            first_is_prime = False
            continue
        if second_current_number > 1:
            for second_number in range(2, second_current_number // 2):
                if(second_current_number % second_number) == 0:
                    second_is_prime = False
                    break
                else:
                    second_is_prime = True
                    second_prime_number = second_current_number
        else:
            second_is_prime = False
            continue
        if first_is_prime and second_is_prime:
            print(f'{first_prime_number}{second_prime_number}')

# test input 10 20 5 5
# test input 10 30 9 6
