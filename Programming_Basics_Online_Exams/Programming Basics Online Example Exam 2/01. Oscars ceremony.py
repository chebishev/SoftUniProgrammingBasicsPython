hall_rent = int(input())

statues = hall_rent * 0.70
catering = statues * 0.85
sound = catering / 2

total = statues + catering + sound + hall_rent

print(f"{total:.2f}")

# test inputs:

# 3500

# 5555
