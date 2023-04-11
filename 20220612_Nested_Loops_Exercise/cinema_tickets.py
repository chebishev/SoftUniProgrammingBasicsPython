command = input()
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while command != "Finish":
    movie = command
    free_seats = int(input())
    seats_counter = 0
    for seats in range(free_seats):
        ticket_type = input()
        if ticket_type == "student":
            student_tickets += 1
            seats_counter += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            seats_counter += 1
        elif ticket_type == "kid":
            kids_tickets += 1
            seats_counter += 1
        else:
            break
    seats_percentage = seats_counter / free_seats * 100
    print(f"{movie} - {seats_percentage:.2f}% full.")
    command = input()

total_tickets = student_tickets + standard_tickets + kids_tickets
student_percentage = student_tickets / total_tickets * 100
standard_percentage = standard_tickets / total_tickets * 100
kids_percentage = kids_tickets / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{student_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kids_percentage:.2f}% kids tickets.")

# test input Taxi
# 10
# standard
# kid
# student
# student
# standard
# standard
# End
# Scary Movie
# 6
# student
# student
# student
# student
# student
# student
# Finish
# test input The Matrix
# 20
# student
# standard
# kid
# kid
# student
# student
# standard
# student
# End
# The Green Mile
# 17
# student
# standard
# standard
# student
# standard
# student
# End
# Amadeus
# 3
# standard
# standard
# standard
# Finish