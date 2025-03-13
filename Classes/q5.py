class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old"
    
        
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def get_grade(self):
        return f"Grade: {self.grade}"
    
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def get_subject(self):
        return f"Subject: {self.subject}"


student1 = Student("Alice", 20, "12th")
teacher1 = Teacher("Mr Smith", 35, "Mathematics")

print(student1.introduce())
print(student1.get_grade())

print(teacher1.introduce())
print(teacher1.get_subject())