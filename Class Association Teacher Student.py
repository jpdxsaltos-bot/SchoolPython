class Teacher:
    def __init__(self, name, teacher_id, subject):
        self.name = name
        self.teacher_ID = teacher_id
        self.subject = subject
        self.students = []
        
    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been added to {self.name}'s class.")

    def remove_student(self, student):
        if student in self.students:
           self.students.remove(student)
           print(f"{student.name} has been removed from {self.name}'s class.")

    def show_attendance(self):
        for student in self.students:
            print(f"{student.name} has attended ")

class Student:
    def __init__(self, name, id, course):
        self.name = name
        self.ID = id
        self.course = course
        self.attendance = []

    def add_student(self, student):
        self.attendance.append(student)
        print(student.name + " is present today " + self.name)

    def remove_student(self, student):
        if student in self.attendance:
            self.attendance.remove(student)
            print(student.name + " was removed from the list " + self.name)
        else:
            print(student.name + " is not present today " + self.name)

    def show_attendance(self):
        for student in self.attendance:
            print(student.name + " is present today " + self.name)

student1 = Student("Jose", 32456, "Student")
student2 = Student("Daniel", 46529, "Student")
student3 = Student("Kostas", 97862, "Student")
student4 = Student("Lac", 87672, "Student")
student5 = Student("Melvin", 89719, "Student")

teacher1 = Teacher("Ope", 86918,"Software")

teacher1.add_student(student1)

teacher1.add_student(student2)

teacher1.add_student(student3)

teacher1.add_student(student4)

teacher1.add_student(student5)

teacher1.show_attendance()

teacher1.remove_student(student3)

teacher1.show_attendance()
