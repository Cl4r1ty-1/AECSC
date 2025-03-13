import statistics

def calculate_average_grades(course_grades):
    grades = [GRADE_VAULES[course_grades["math"]], GRADE_VAULES[course_grades["science"]], GRADE_VAULES[course_grades["history"]]]
    return statistics.median(grades)

GRADE_VAULES = {'A':4, 'B':3, 'C':2, 'D':1, 'F':0}

course_grades = {
    "math":"A",
    "science":"B",
    "history":"C"
}

average_grade = calculate_average_grades(course_grades)

for grade, number in GRADE_VAULES.items():
    if average_grade == number:
        average_grade = grade

print(f"Average Grade (median): {average_grade}")