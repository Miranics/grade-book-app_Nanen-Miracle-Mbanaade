# gradebook.py

from grade_book_app.student.student import Student  # Import Student class from student folder
from grade_book_app.course.course import Course  # Import Course class from course folder

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, first_name, last_name):
        student = Student(email, first_name, last_name)
        self.student_list.append(student)

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name):
        student = self.find_student(student_email)
        course = self.find_course(course_name)
        if student and course:
            student.register_for_course(course)

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()

    def calculate_ranking(self):
        ranked_students = sorted(self.student_list, key=lambda s: s.calculate_GPA(), reverse=True)
        for i, student in enumerate(ranked_students):
            print(f"{i+1}. {student} - GPA: {student.calculate_GPA():.2f}")

    def search_by_grade(self, min_grade, max_grade):
        matching_students = []
        for student in self.student_list:
            for grade in student.grades.values():
                if grade is not None and min_grade <= grade <= max_grade:
                    matching_students.append(student)
                    break  # Only need first occurrence per student
        if matching_students:
            print("Students with grades between", min_grade, "and", max_grade)
            for student in matching_students:
                print(student)
        else:
            print("No students found with grades between", min_grade, "and", max_grade)

    def generate_transcript(self, student_email):
        student = self.find_student(student_email)
        if student:
            print(f"Transcript for: {student}")
            print("Course\t Trimester\t Credits\t Grade")
            for course in student.courses_registered:
                grade = student.grades.get(course)
                print(f"{course.name}\t {course.trimester}\t {course.credits}\t {grade}")

    def find_student(self, email):
        for student in self.student_list:
            if student.email == email:
                return student
        return None

    def find_course(self, name):
        for course in self.course_list:
            if course.name == name:
                return course
        return None
