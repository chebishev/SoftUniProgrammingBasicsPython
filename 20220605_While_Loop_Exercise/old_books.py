book_name = input()
checked_books = 0
is_book_found = False
current_book = input()

while current_book != "No More Books":
    if current_book == book_name:
        is_book_found = True
        print(f"You checked {checked_books} books and found it.")
        break

    checked_books += 1
    current_book = input()

if not is_book_found:
     print("The book you search is not here!")
     print(f'You checked {checked_books} books.')

# test input Troy Stronger Life Style Troy
# test input The spot Hunger Games Harry Potter Torronto Spotify No More Books
# test input Bourne True Story Forever More Space The Girl Spaceship Strongest Profit Tripple Stella The Matrix Bourne
