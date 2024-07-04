movie_name = input()
hall_type = input()
bought_tickets = int(input())

price_types = ["normal", "luxury", "ultra luxury"]
price_index = price_types.index(hall_type)
movie_dictionary = {
    "A Star Is Born": [7.50, 10.50, 13.50],
    "Bohemian Rhapsody": [7.35, 9.45, 12.75],
    "Green Book": [8.15, 10.25, 13.25],
    "The Favourite": [8.75, 11.55, 13.95]
}
total_price = movie_dictionary[movie_name][price_index] * bought_tickets
print(f'{movie_name} -> {total_price:.2f} lv.')

# test inputs:

# A Star Is Born
# luxury
# 42

# Green Book
# normal
# 63
