building_floors = int(input())
rooms_per_floor = int(input())

for floors in range(building_floors, 0, -1):
    floor_type = ""
    for rooms in range(rooms_per_floor):
        if floors == building_floors:
            floor_type = "L"
        elif floors % 2 == 0:
            floor_type = "O"
        else:
            floor_type = "A"
        print(f'{floor_type}{floors}{rooms}', end=" ")
    print()
