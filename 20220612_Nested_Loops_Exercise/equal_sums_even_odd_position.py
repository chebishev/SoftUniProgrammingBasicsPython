start = int(input())
end = int(input())

for numbers in range(start, end + 1):
    odd_sum = 0
    even_sum = 0
    conversion = str(numbers)
    for index, digit in enumerate(conversion):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if odd_sum == even_sum:
        print(numbers, end=" ")

# test input 100000 100050
# test input 123456 124000
# test input 299000 300000
# test input 100115 100120
