nylon = int(input()) + 2
paint_in_liters = int(input())
thinner_in_liters = int(input())
working_hours = int(input())

nylon_total = nylon * 1.5
paint_total = (paint_in_liters + (paint_in_liters * 0.1)) * 14.50
thinner_total = thinner_in_liters * 5

total_materials = nylon_total + paint_total + thinner_total + 0.40
work_price = (total_materials * 0.30) * working_hours
total = total_materials + work_price

print(total)

# test input 10 11 4 8
# test input 5 10 10 1
