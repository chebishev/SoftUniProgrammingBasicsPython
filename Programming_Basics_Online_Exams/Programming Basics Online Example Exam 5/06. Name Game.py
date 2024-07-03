command = input()
winner = ""
max_points = 0

while command != "Stop":
    player_name = command
    points = 0
    for letter in player_name:
        ascii_value = ord(letter)
        number_for_compare = int(input())

        if ascii_value == number_for_compare:
            points += 10
        else:
            points += 2

    if points >= max_points:
        max_points = points
        winner = player_name

    command = input()

print(f"The winner is {winner} with {max_points} points!")

# test inputs:

# Ivan
# 73
# 20
# 98
# 110
# Ivo
# 80
# 65
# 87
# Stop

# Pesho
# 124
# 34
# 111
# 97
# 99
# Gosho
# 98
# 124
# 88
# 76
# 18
# Stop
