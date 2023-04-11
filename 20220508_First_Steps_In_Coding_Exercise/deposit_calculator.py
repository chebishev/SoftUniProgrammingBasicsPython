deposit_total = float(input())
deposit_term = int(input())
annual_interest_rate = float(input()) / 100

interest = deposit_total * annual_interest_rate
monthly_interest  = interest / 12
total = deposit_total + (deposit_term * monthly_interest)

print(total)

# test input 200 3 5.7
# test input 2350 6 7
