bad_grades = int(input())
problems_count = 0
last_problem = ""
bad_attempts = 0
score = 0

while True:
    command = input()
    if command == "Enough":
        break
    grade = int(input())
    score += grade
    problems_count += 1
    last_problem = command

    if grade <= 4:
        bad_attempts += 1
        if bad_attempts == bad_grades:
            break

average_score = score / problems_count
if bad_attempts == bad_grades:
    print(f"You need a break, {bad_attempts} poor grades.")
else:
    print(f"Average score: {average_score:.2f}")
    print(f'Number of problems: {problems_count}')
    print(f'Last problem: {last_problem}')

# test input 3 Money 6 Story 4 Spring Time 5 Bus 6 Enough
# test input 2 Income 3 Game Info 6 Best Player 4
