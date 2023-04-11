one_lev = int(input())
two_levs = int(input())
five_levs= int(input())
total_sum = int(input())
one_Lev_count = 0
two_levs_count = 0
five_levs_count = 0
total_twos = 0
total_fives = 0

for ones in range(1, one_lev+1):
    one_Lev_count += 1
    for twos in range(1, two_levs+1):
        total_twos = 2 * twos
        two_levs_count += 1
        for fives in range(1, five_levs+1):
            total_fives = 5 * fives
            five_levs_count += 1
            if ones + total_twos + total_fives == total_sum:
                print(f"{one_Lev_count} * 1 lv. + {total_twos} * 2 lv. + {total_fives} * 5 lv. = {total_sum} lv.")

# test input 3 2 3 10
# test input 5 3 1 7
