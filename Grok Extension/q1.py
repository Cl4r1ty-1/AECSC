def calculate_average_grade(grades):
    return sum(grades.values())/len(grades.values())

def get_highest_grade(grades):
    grade = ["", 0]
    for key, value in grades.items():
        if grade[1] < value:
            grade[0] = key
            grade[1] = value
    return grade

grades = {}

num_of_students = int(input("Enter number of students: "))

while len(grades.keys()) < num_of_students:
    name = input("Enter student name: ")
    grade = int(input(f"Enter {name}'s grade: "))
    grades[name] = grade

average_grade = calculate_average_grade(grades)
highest_grade = get_highest_grade(grades)

print()
print(f"Average grade: {average_grade}")
print(f"Highest grade: {highest_grade[0]} with {highest_grade[1]}")
print("Student Grades:")
for name, grade in grades.items():
    print(f"{name}: {grade}")
