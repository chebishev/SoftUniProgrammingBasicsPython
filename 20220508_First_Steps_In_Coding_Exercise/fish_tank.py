length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

volume = length * width * height
liters = volume * 0.001
needed_liters = liters * (1 - percent)

print(needed_liters)

# test input 85 75 47 17
# test input 105 77 89 18.5
