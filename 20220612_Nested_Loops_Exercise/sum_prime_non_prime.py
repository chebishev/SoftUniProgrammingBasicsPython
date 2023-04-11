command = input()
sum_prime_numbers = 0
sum_non_prime_numbers = 0
counter = 0

while command != "stop":
    number = int(command)
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    for numbers in range(1, number+1):
        if number % numbers == 0:
            counter += 1
    if counter > 2:
        sum_non_prime_numbers += number
    else:
        sum_prime_numbers += number
    counter = 0
    command = input()

print(f"Sum of all prime numbers is: {sum_prime_numbers}")
print(f'Sum of all non prime numbers is: {sum_non_prime_numbers}')

# test input 3 9 0 7 19 4 stop
# test input 30 83 33 -1 20 stop
# test input 0 -9 0 stop
