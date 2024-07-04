movies_count = int(input())
max_rating = 0
max_movie = ""
min_rating = 11
min_movie = ""
total_rating = 0

for _ in range(movies_count):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating

    if movie_rating > max_rating:
        max_rating = movie_rating
        max_movie = movie_name

    if movie_rating < min_rating:
        min_rating = movie_rating
        min_movie = movie_name

print(f"{max_movie} is with highest rating: {max_rating}")
print(f"{min_movie} is with lowest rating: {min_rating}")

average_rating = total_rating / movies_count
print(f"Average rating: {average_rating:.1f}")

# test inputs:

# 5
# A Star is Born
# 7.8
# Creed 2
# 7.3
# Mary Poppins
# 7.2
# Vice
# 7.2
# Captain Marvel
# 7.1

# 3
# Interstellar
# 8.5
# Dangal
# 8.3
# Green Book
# 8.2
