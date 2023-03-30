class Student:
    def __init__(self, name, roll_no, grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

class StudentRecordSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student) #add_student(Student("abc",10,A+))

    def remove_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)

    def get_student_by_roll_no(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                return student
        return None

    def get_all_students(self):
        return self.students




# Create a new student record system
record_system = StudentRecordSystem()  #students = [] 
# with the help of this object we can access all the functions of the class.

# Add some students
student1 = Student("Abdul", 1, "A+")  #{"name":"Abdul","roll_no":1,"grade":"A+"}
record_system.add_student(student1)  #students = [{"name":"Abdul","roll_no":1,"grade":"A+"},
#                                                 {"name":"Mahesh","roll_no":2,"grade":"A"},
#                                                 {"name":"Pushpak","roll_no":3,"grade":"B+"}]

student2 = Student("Mahesh", 2, "A")
record_system.add_student(student2)

student3 = Student("Pushpak", 3, "B+")
record_system.add_student(student3)

# Get a student by their roll no
print(record_system.get_student_by_roll_no(2).name) # Output: "Mahesh"


#Remove a student
record_system.remove_student(5)
# print(len(record_system.get_all_students()))


#Get all students again
for student in record_system.get_all_students():
    print(student.name, student.roll_no, student.grade)

