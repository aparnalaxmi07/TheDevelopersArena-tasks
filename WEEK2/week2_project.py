# ---------------------------------------------------------
# WEEK 2 PROJECT: STUDENT GRADE CALCULATOR
# Developer's Arena Internship
# ---------------------------------------------------------

print("===== Student Grade Calculator =====")

# Store all results in a list
results = []

while True:
    name = input("Enter student name (or 'exit' to quit): ")
    if name.lower() == "exit":
        break

    try:
        marks = float(input("Enter marks (0–100): "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Determine grade and comment
    if marks >= 90:
        grade = "A"
        comment = "Excellent performance"
    elif marks >= 75:
        grade = "B"
        comment = "Good job"
    elif marks >= 60:
        grade = "C"
        comment = "Satisfactory"
    elif marks >= 40:
        grade = "D"
        comment = "Needs improvement"
    else:
        grade = "F"
        comment = "Failed"

    results.append((name, marks, grade, comment))
    print(f"{name} - Grade: {grade} ({comment})")

print("\n===== Final Results =====")
for student in results:
    print(f"Name: {student[0]} | Marks: {student[1]} | Grade: {student[2]} | Comment: {student[3]}")

print("--------------------------------------")
print("Thank you for using the Grade Calculator!")
print("--------------------------------------")
