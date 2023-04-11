book_pages = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

book_time = book_pages // pages_per_hour
hours_per_day = book_time // days_per_book

print(hours_per_day)

# test input 212 20 2
# test input 432 15 4
