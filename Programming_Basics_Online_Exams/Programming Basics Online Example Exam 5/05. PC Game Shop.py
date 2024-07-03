sold_games_count = int(input())
games = {
    "Hearthstone": 0,
    "Fornite": 0,
    "Overwatch": 0,
    "Others": 0
}

for game in range(1, sold_games_count + 1):
    game_name = input()
    if game_name in games:
        games[game_name] += 1
    else:
        games["Others"] += 1

for sold_game, count in games.items():
    percentage = count / sold_games_count * 100
    print(f"{sold_game} - {percentage:.2f}%")

# test inputs:

# 4
# Hearthstone
# Fornite
# Overwatch
# Counter-Strike
