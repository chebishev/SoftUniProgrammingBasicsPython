flour_price_for_kg = float(input())
flour_in_kilos = float(input())
sugar_in_kilos = float(input())
eggs_peels = int(input())
yeast_packets = int(input())

sugar_price = flour_price_for_kg * 0.75
eggs_price = flour_price_for_kg * 1.1
yeast_price = sugar_price * 0.2

total = (flour_price_for_kg * flour_in_kilos +
         sugar_price * sugar_in_kilos +
         eggs_price * eggs_peels +
         yeast_price * yeast_packets)
print(f'{total:.2f}')

# test inputs:

# 50
# 10
# 3.5
# 6
# 1

# 63.44
# 3.57
# 6.35
# 8
# 2
