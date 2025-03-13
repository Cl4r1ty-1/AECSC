student = {
    "name":"Alice",
    "age":20,
    "major":"Computer Science"
}

student["gpa"] = 3.5

course_grades = {
    "math":"A",
    "science":"B",
    "history":"C"
}

student_info = student | course_grades
print(student_info)