tournament_days = int(input())
winning_days = 0
total_money = 0

for day in range(1, tournament_days + 1):
    wins = 0
    loses = 0

    command = input()
    while command != "Finish":
        sport = command
        result = input()
        if result == "win":
            wins += 1
        else:
            loses += 1

        command = input()

    daily_money = wins * 20
    if wins > loses:
        winning_days += 1
        daily_money *= 1.10

    total_money += daily_money

if winning_days > tournament_days / 2:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")

# test inputs:

# 2
# volleyball
# win
# football
# lose
# basketball
# win
# Finish
# golf
# win
# tennis
# win
# badminton
# win
# Finish

# 3
# darts
# lose
# handball
# lose
# judo
# win
# Finish
# snooker
# lose
# swimming
# lose
# squash
# lose
# table tennis
# win
# Finish
# volleyball
# win
# basketball
# win
# Finish
