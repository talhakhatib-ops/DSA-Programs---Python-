# Program to calculate a student's average and grade

marks = []

for subject in range(1, 6):
    mark = float(input(f"Enter marks for subject {subject} (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        break
    marks.append(mark)

if len(marks) == 5:
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Total marks:", sum(marks))
    print("Average:", round(average, 2))
    print("Grade:", grade)
