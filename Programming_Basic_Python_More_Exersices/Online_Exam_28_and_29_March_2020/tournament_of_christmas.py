tournament_days = int(input())
command = input()
win_counter = 0
lose_counter = 0
days_win = 0
days_lose = 0
raised_money = 0
for day in range(1, tournament_days + 1):
    daily_raised_money = 0
    while command != "Finish":
        sport = command
        command = input()
        if command == "win":
            win_counter += 1
            daily_raised_money += 20
        else:
            lose_counter += 1
        command = input()
    if win_counter > lose_counter:
        daily_raised_money *= 1.10
        days_win += 1
    else:
        days_lose += 1
    raised_money += daily_raised_money
    win_counter = 0
    lose_counter = 0
    if day == tournament_days:
        break
    else:
        command = input()
if days_win > days_lose:
    raised_money *= 1.20
    print(f"You won the tournament! Total raised money: {raised_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {raised_money:.2f}")

# test input 2 volleyball win football lose basketball win Finish golf win tennis win badminton win Finish
# test input 3 darts lose handball lose judo win Finish snooker lose swimming lose squash lose table tennis win Finish
# volleyball win basketball win Finish
