easter_breads_count = int(input())
eggs_peels_count = int(input())
cookies_in_kg = int(input())

total_easter_breads = easter_breads_count * 3.20
total_eggs = eggs_peels_count * 4.35
total_eggs_paint = eggs_peels_count * 12 * 0.15
total_cookies = cookies_in_kg * 5.40

total = total_easter_breads + total_eggs + total_eggs_paint + total_cookies
print(f"{total:.2f}")

# test inputs:

# 3
# 2
# 3

# 4
# 4
# 3
