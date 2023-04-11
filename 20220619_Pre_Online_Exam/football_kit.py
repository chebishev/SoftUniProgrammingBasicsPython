t_shirt_price = float(input())
target_sum = float(input())
spend_money = 0
shorts_price = t_shirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = (shorts_price + t_shirt_price) * 2
spend_money = (t_shirt_price + shorts_price + socks_price + shoes_price) * 0.85


if spend_money >= target_sum:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {spend_money:.2f} lv.")
else:
    diff = target_sum - spend_money
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")

