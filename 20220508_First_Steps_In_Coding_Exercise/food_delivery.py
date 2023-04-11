chicken_menu_price = int(input()) * 10.35
fish_menu_price = int(input()) * 12.40
vegetarian_menu_price = int(input()) * 8.15

all_menus_price = chicken_menu_price + fish_menu_price + vegetarian_menu_price
desert_price = all_menus_price * 0.20
total = all_menus_price + desert_price + 2.50

print(f'{total:.2f}')
# test input 2 4 3
# test input 9 2 3
