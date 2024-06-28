possible_fruits = {
    "Watermelon": {"small": 2 * 56, "big": 5 * 28.70},
    "Mango": {"small": 2 * 36.66, "big": 5 * 19.60},
    "Pineapple": {"small": 2 * 42.10, "big": 5 * 24.80},
    "Raspberry": {"small": 2 * 20, "big": 5 * 15.20}
}

fruit = input()
set_size = input()
ordered_sets_count = int(input())

total = possible_fruits[fruit][set_size] * ordered_sets_count
if 400 <= total <= 1000:
    total *= 0.85
elif total > 1000:
    total *= 0.50
print(f"{total:.2f} lv.")


# test inputs:
# Watermelon
# big
# 4

# Pineapple
# small
# 1
