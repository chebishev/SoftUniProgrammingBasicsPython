locations = int(input())

for location in range(locations):
    average_extraction_expected = float(input())
    days_for_location = int(input())
    total_gold = 0
    for day in range(days_for_location):
        extracted_gold = float(input())
        total_gold += extracted_gold
    average_per_day = total_gold / days_for_location
    if average_per_day >= average_extraction_expected:
        print(f"Good job! Average gold per day: {average_per_day:.2f}.")
    else:
        diff = average_extraction_expected - average_per_day
        print(f"You need {diff:.2f} gold.")

# test input 2 10 3 10 10 11 20 2 20 10
# test input 1 5 3 10 1 3
