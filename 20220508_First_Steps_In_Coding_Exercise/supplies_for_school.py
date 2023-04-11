pen_packets_price = int(input()) * 5.80
marker_packets_price = int(input()) * 7.20
cleaner_liter_price = int(input()) * 1.20
discount_percent = int(input()) / 100

total = pen_packets_price + marker_packets_price + cleaner_liter_price
total_with_discount = total - (total * discount_percent)

print(total_with_discount)

# test input 2 3 4 25
# test input 4 5 5 10
