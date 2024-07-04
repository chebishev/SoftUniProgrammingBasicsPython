voucher_value = int(input())
bought_tickets = 0
bought_others = 0
is_movie_ticket = False

command = input()
while command != "End":
    if len(command) > 8:
        price = ord(command[0]) + ord(command[1])
        is_movie_ticket = True
    else:
        price = ord(command[0])

    if voucher_value - price < 0:
        break

    if is_movie_ticket:
        bought_tickets += 1
    else:
        bought_others += 1

    voucher_value -= price
    is_movie_ticket = False

    command = input()

print(bought_tickets)
print(bought_others)

# test inputs:

# 300
# Captain Marvel
# popcorn
# Pepsi

# 1500
# Avengers: Endgame
# Bohemian Rhapsody
# Deadpool 2
# End
