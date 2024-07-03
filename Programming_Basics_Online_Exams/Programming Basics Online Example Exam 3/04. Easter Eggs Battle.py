player_one_eggs = int(input())
player_two_eggs = int(input())

command = input()
while command != "End":
    if command == "one":
        player_two_eggs -= 1
        if player_two_eggs == 0:
            print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
            break
    elif command == "two":
        player_one_eggs -= 1
        if player_one_eggs == 0:
            print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
            break

    command = input()
else:
    print(f"Player one has {player_one_eggs} eggs left.")
    print(f"Player two has {player_two_eggs} eggs left.")

# test inputs:

# 5
# 4
# one
# two
# one
# two
# two
# End

# 2
# 6
# one
# two
# two

# 6
# 3
# one
# two
# two
# one
# one
