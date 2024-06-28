football_team_name = input()
played_games = int(input())
result_counter = {
    "W": 0,
    "D": 0,
    "L": 0
}
points = 0

if played_games == 0:
    print(f"{football_team_name} hasn't played any games during this season.")
else:
    for match in range(played_games):
        result = input()
        if result == "W":
            points += 3
        elif result == "D":
            points += 1
        else:
            points += 0
        result_counter[result] += 1

    print(f"{football_team_name} has won {points} points during this season.")
    print("Total stats:")
    for result_type, count in result_counter.items():
        print(f"## {result_type}: {count}")

    print(f"Win rate: {result_counter['W'] / played_games * 100:.2f}%")

# test inputs:

# Liverpool
# 10
# W
# D
# D
# W
# L
# W
# D
# D
# W
# W

# Barcelona
# 7
# W
# D
# L
# L
# W
# W
# D

# Chelsea
# 0
