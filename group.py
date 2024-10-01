from student import Student

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    # def __str__(self):
    #     return f"Group {self.number}:\n" + "\n".join([str(student) for student in self.group])

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
            all_students += str(student)
        return f"Group {self.number}:\n{all_students}"