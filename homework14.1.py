class MoreThanExpected(Exception):
    def __init__(self, message):
        self.message = message

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender}, {self.age},{self.first_name}, {self.last_name}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.gender}, {self.age},{self.first_name}, {self.last_name},{self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise MoreThanExpected ("You are trying to add more than 10 students")
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_remove = None
        for student in self.group:
            if student.last_name == last_name:
                student_to_remove = student
                break
        if student_to_remove:
            self.group.remove(student_to_remove)
        else:
            print("# No error!")


    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students = all_students + str(student) + "\n"
        return f"Group {self.number}:\n{all_students}"

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN143')
st3 = Student('Female', 23, 'Karl', 'Belton', 'AN144')
st4 = Student('Male', 67, 'Mark', 'Mueller', 'AN145')
st5 = Student('Female', 36, 'Anna', 'Weiss', 'AN146')
st6 = Student('Male', 24, 'John', 'Sneha', 'AN147')
st7 = Student('Male', 19, 'Kerry', 'Suma', 'AN148')
st8 = Student('Male', 27, 'Linda', 'Jacob', 'AN149')
st9 = Student('Male', 91, 'Rick', 'Menon', 'AN150')
st10 = Student('Female', 6, 'Laura', 'Aaron', 'AN151')
st11 = Student('Female', 46, 'Mukhamed', 'Pathak', 'AN152')
gr = Group('PD1')
try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)

except MoreThanExpected as e:
    print(e)

print(gr)

