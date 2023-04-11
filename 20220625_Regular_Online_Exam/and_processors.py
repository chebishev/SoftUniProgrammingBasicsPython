processors_needed = int(input())
employees = int(input())
working_days = int(input())

# 3 hours per processor
# 8 hours per day per employee

all_working_time = employees * working_days * 8
processors_made = int(all_working_time / 3)
diff = abs(processors_needed - processors_made)
total = diff * 110.10
if processors_made < processors_needed:
    print(f"Losses: -> {total:.2f} BGN")
else:
    profit = processors_made * 110
    print(f"Profit: -> {total:.2f} BGN")

# test input 500 8 20
# test input 150 7 18
