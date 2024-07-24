#!/usr/bin/env python3
#grade_book_app/grade book.py

from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def register_student_for_course(self, email, course_name, grade):
        student = next((s for s in self.student_list if s.email == email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
            student.calculate_GPA()  # Recalculate GPA after registration
        else:
            raise ValueError("Invalid student email or course name")

    def calculate_GPA(self, email):
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            return student.calculate_GPA()
        else:
            raise ValueError("Invalid student email")

    def calculate_ranking(self):
        self.student_list.sort(key=lambda s: s.GPA, reverse=True)
        return self.student_list

    def search_by_grade(self, grade):
        students_with_grade = [student for student in self.student_list 
                               if grade in student.courses_registered.values()]
        return students_with_grade

    def generate_transcript(self, email):
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            transcript = {
                "names": student.names,
                "email": student.email,
                "GPA": student.GPA,
                "courses": [(course.name, grade) for course, grade in student.courses_registered.items()]
            }
            return transcript
        else:
            raise ValueError("Invalid student email")
