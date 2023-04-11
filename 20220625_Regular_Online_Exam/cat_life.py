breed = input()
sex = input()
years = 0
is_invalid = False
if breed == "British Shorthair":
    if sex == "m":
        years = 13
    else:
        years = 14
elif breed == "Siamese":
    if sex == "m":
        years = 15
    else:
        years = 16
elif breed == "Persian":
    if sex == "m":
        years = 14
    else:
        years = 15
elif breed == "Ragdoll":
    if sex == "m":
        years = 16
    else:
        years = 17
elif breed == "American Shorthair":
    if sex == "m":
        years = 12
    else:
        years = 13
elif breed == "Siberian":
    if sex == "m":
        years = 11
    else:
        years = 12
else:
    is_invalid = True

cat_months = int((years * 12) / 6)
if is_invalid:
    print(f"{breed} is invalid cat!")
else:
    print(f"{cat_months} cat months")

# test input Persian m
# test input Siamese f
# test input Siberian m
# test input Ragdoll f
# test input Tom m
