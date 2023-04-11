cpu_price = float(input())
gpu_price = float(input())
ram_price = float(input())
ram_quantity = int(input())
discount_percent = float(input())
total = 0
dollar_to_lev = 1.57

ram_total = ram_price * ram_quantity
discount = (cpu_price + gpu_price) * discount_percent
total = cpu_price + gpu_price + ram_total - discount
total *= dollar_to_lev

print(f"Money needed - {total:.2f} leva.")
