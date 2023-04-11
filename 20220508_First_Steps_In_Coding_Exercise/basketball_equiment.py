annual_fee = int(input())

snickers_price = annual_fee - (annual_fee * 0.4)
outfit = snickers_price - (snickers_price * 0.2)
ball = outfit / 4
accessories = ball / 5

total = annual_fee + snickers_price + outfit + ball + accessories

print(total)

# test input 365
# test input 550
