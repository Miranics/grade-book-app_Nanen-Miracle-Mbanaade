#!/usr/bin/env python3
#grade_book_app/grade book.py

import json
from student import Student
from course import Course

class GradeBook:
    def __init__(self, students_file='students.json', courses_file='courses.json'):
        self.students_file = students_file
        self.courses_file = courses_file
        self.student_list = self.load_students()
        self.course_list = self.load_courses()

    def add_student(self, email, names):
        # Add a new student and save the updated student list
        student = Student(email, names)
        self.student_list.append(student)
        self.save_students()

    def delete_student(self, email):
        # Delete a student by their email and save the updated student list
        self.student_list = [student for student in self.student_list if student.email != email]
        self.save_students()

    def add_course(self, name, trimester, credits):
        # Add a new course and save the updated course list
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        self.save_courses()

    def register_student_for_course(self, email, course_name, grade):
        # Register a student for a course and update their GPA
        student = next((s for s in self.student_list if s.email == email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
            self.save_students()
        else:
            raise ValueError("Invalid student email or course name")

    def calculate_GPA(self, email):
        # Calculate the GPA for a specific student
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            return student.calculate_GPA()
        else:
            raise ValueError("Invalid student email")

    def calculate_ranking(self):
        # Calculate and return student ranking based on GPA
        # Update GPA for all students before ranking
        for student in self.student_list:
            student.calculate_GPA()
        # Sort students by GPA in descending order
        sorted_students = sorted(self.student_list, key=lambda s: s.GPA, reverse=True)
        return sorted_students

    def search_by_grade(self, grade):
        # Search for students by a specific grade
        students_with_grade = [student for student in self.student_list 
                               if grade in student.courses_registered.values()]
        return students_with_grade

    def generate_transcript(self, email):
        # Generate a transcript for a specific student
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

    def view_all_students(self):
        # Return the list of all registered students
        return self.student_list

    def save_students(self):
        # Save the student list to a JSON file
        with open(self.students_file, 'w') as file:
            json.dump([student.to_dict() for student in self.student_list], file)

    def load_students(self):
        # Load the student list from a JSON file
        try:
            with open(self.students_file, 'r') as file:
                data = json.load(file)
                return [Student.from_dict(student, self.course_list) for student in data]
        except FileNotFoundError:
            return []

    def save_courses(self):
        # Save the course list to a JSON file
        with open(self.courses_file, 'w') as file:
            json.dump([course.to_dict() for course in self.course_list], file)

    def load_courses(self):
        # Load the course list from a JSON file
        try:
            with open(self.courses_file, 'r') as file:
                data = json.load(file)
                return [Course.from_dict(course) for course in data]
        except FileNotFoundError:
            return []
