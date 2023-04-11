change = float(input()) * 100
coins = 0
hundreds = int(change % 1000)

while hundreds != 0:
    if hundreds >= 200:
        coins += 1
        hundreds -= 200
        continue
    if hundreds >= 100:
        coins += 1
        hundreds -= 100
        continue
    if hundreds >= 50:
        coins += 1
        hundreds -= 50
        continue
    if hundreds >= 20:
        coins += 1
        hundreds -= 20
        continue
    if hundreds >= 10:
        coins += 1
        hundreds -= 10
        continue
    if hundreds >= 5:
        coins += 1
        hundreds -= 5
        continue
    if hundreds >= 2:
        coins += 1
        hundreds -= 2
        continue
    if hundreds >= 1:
        coins += 1
        hundreds -= 1
        continue

print(coins)

# test input 1.23
# test input 2
# test input 0.56
# test input 2.73
