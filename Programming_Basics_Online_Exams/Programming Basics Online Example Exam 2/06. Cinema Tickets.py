command = input()
total_tickets = 0
ticket_types = {
    "student": 0,
    "standard": 0,
    "kid": 0
}

while command != "Finish":
    available_seats = int(input())
    real_seats = 0
    for _ in range(available_seats):
        ticket_type = input()
        if ticket_type == "End":
            break
        total_tickets += 1
        ticket_types[ticket_type] += 1
        real_seats += 1

    seats_percentage = real_seats / available_seats * 100
    print(f"{command} - {seats_percentage:.2f}% full.")

    command = input()

print(f"Total tickets: {total_tickets}")

for type, count in ticket_types.items():
    percentage = count / total_tickets * 100
    type = "kids" if type == "kid" else type
    print(f"{percentage:.2f}% {type} tickets.")

# test inputs:

# Taxi
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

# The Matrix
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
