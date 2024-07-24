#!/usr/bin/env python3
#grade_book_app/grade book.py

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def add_course(self, course):
        self.course_list.append(course)

    def register_student_for_course(self, student, course):
        student.register_for_course(course)

    def calculate_GPA(self, student):
        student.calculate_GPA()

    def calculate_ranking(self):
        # Logic to calculate ranking
        pass

    def search_by_grade(self, grade):
        # Logic to search by grade
        pass

    def generate_transcript(self, student):
        # Logic to generate transcript
        pass
