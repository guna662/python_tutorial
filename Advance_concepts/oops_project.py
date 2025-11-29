# Step 1 — Create a Student Class
class Student:
    def _init_(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, in grade {self.grade}."

# Step 2 — Teacher Class (Inheritance)
class Teacher(Student):
    def _init_(self, name, age, subject):
        super()._init_(name, age, grade=None)  # teacher has no grade
        self.subject = subject

    def introduce(self):
        return f"Hello, I'm {self.name}, and I teach {self.subject}."
    
#     Step 3 — Classroom (Composition)

# A classroom contains many students and 1 teacher.

# Classroom = has-a (composition)

class Classroom:
    def _init_(self, class_name, teacher):
        self.class_name = class_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def classroom_info(self):
        print(f"Classroom: {self.class_name}")
        print("Teacher:", self.teacher.introduce())
        print("Students:")
        for s in self.students:
            print(" -", s.introduce())

# Step 4 — School (Big Level)
# A school has many classrooms.
# This joins the entire project together.

class School:
    def _init_(self, name):
        self.name = name
        self.classrooms = []

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def school_info(self):
        print(f"Welcome to {self.name} School")
        print("---- Classrooms ----")
        for c in self.classrooms:
            c.classroom_info()
            print("--------------------")

# Step 5 — Encapsulation Example

# We hide the student’s marks and allow safe access.
class Marks:
    def _init_(self):
        self.__marks = 0   # private variable

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")

    def get_marks(self):
        return self.__marks
    


    # Create Teacher
t1 = Teacher("Mr. Sharma", 40, "Maths")

# Create Students
s1 = Student("Amit", 12, 7)
s2 = Student("Riya", 13, 7)
s3 = Student("Kiran", 12, 7)

# Create Classroom
class7A = Classroom("7A", t1)
class7A.add_student(s1)
class7A.add_student(s2)
class7A.add_student(s3)

# Create School
school = School("Sunshine")
school.add_classroom(class7A)

# Show info
school.school_info()