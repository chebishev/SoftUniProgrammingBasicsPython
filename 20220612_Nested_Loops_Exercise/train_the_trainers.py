people_in_jury = int(input())
command = input()
total_grades = 0
average_grades = 0

while command != "Finish":
    presentation = command
    presentation_grade = 0
    average_grade = 0
    for grades in range(people_in_jury):
        grade = float(input())
        presentation_grade += grade
        total_grades += grade
    average_grade = presentation_grade / people_in_jury
    average_grades += 1
    print(f"{presentation} - {average_grade:.2f}.")
    command = input()

total_average_grade = (total_grades / average_grades) / people_in_jury
print(f"Student's final assessment is {total_average_grade:.2f}.")

# test input 2 While-Loop 6.00 5.50 For-Loop 5.84 5.66 Finish
# test input 3 Arrays 4.53 5.23 5.00 Lists 5.83 6.00 5.42 Finish
# test input 2 Objects and Classes 5.77 4.23 Dictionaries 4.62 5.02 RegEx 2.88 3.42 Finish
