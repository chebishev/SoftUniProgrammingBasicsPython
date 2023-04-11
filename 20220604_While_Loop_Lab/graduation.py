name = input()
grade = 1
total_grades = 0
fails = 0

while True:
    grades = float(input())
    if grade == 13:
        break
    if grades < 4:
        fails += 1
        if fails > 1:
            break
    else:
        total_grades += grades
        grade += 1
if fails > 1:
    print(f"{name} has been excluded at {grade} grade")
else:
    average_grade = total_grades / 12
    print(f'{name} graduated. Average grade: {average_grade:.2f}')
