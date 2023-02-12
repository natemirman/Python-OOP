from tests import test_SoftwareStudent_constructor, test_SoftwareStudent_get_major, test_SoftwareStudent_get_greeting, test_SoftwareStudent_calculate_workload
from student import Student

class SoftwareStudent(Student):
    def __init__(self, name, birth_year, student_id, credit_hours, major):
        Student.__init__(self, name, birth_year, student_id, credit_hours)
        self.major = major

    def get_major(self):
        return self.major

    def get_greeting(self):
        return "Hello, my name is " + self.name + " and I am a " + self.major + " major."

    def calculate_workload(self):
        return self.credit_hours*3+10

def main():

    names_list = ["John", "Jane", "Joe", "Jill"]
    birthyear_list = [1990, 1991, 1992, 1993]
    student_id_list = ["12345", "23456", "34567", "45678"]
    credit_hours_list = [6, 9, 12, 15]
    major_list = ["Computer Science", "Computer Engineering",
                  "Information Technology", "Software Engineering"]

    student_list = [
        SoftwareStudent(names_list[0], birthyear_list[0], student_id_list[0], credit_hours_list[0], major_list[0]),
        SoftwareStudent(names_list[1], birthyear_list[1], student_id_list[1], credit_hours_list[1], major_list[1]),
        SoftwareStudent(names_list[2], birthyear_list[2], student_id_list[2], credit_hours_list[2], major_list[2]),
        SoftwareStudent(names_list[3], birthyear_list[3], student_id_list[3], credit_hours_list[3], major_list[3]),
    ]

    test_SoftwareStudent_constructor(names_list, birthyear_list, student_id_list, credit_hours_list, major_list, student_list)
    test_SoftwareStudent_get_major(major_list, student_list)
    test_SoftwareStudent_get_greeting(names_list, major_list, student_list)
    test_SoftwareStudent_calculate_workload(credit_hours_list, student_list)

    print("All tests passed!")


if __name__ == "__main__":
    main()