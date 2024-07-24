#!/usr/bin/env python3
class Student:
    def __init__(self, email, names, courses_registered=None, GPA=0.0):
        self.email = email
        self.names = names
        self.courses_registered = courses_registered if courses_registered else {}
        self.GPA = GPA

    def calculate_GPA(self):
        # Calculate the GPA based on registered courses and grades
        total_points = 0
        total_credits = 0
        for course, grade in self.courses_registered.items():
            total_points += grade * course.credits
            total_credits += course.credits
        self.GPA = total_points / total_credits if total_credits != 0 else 0.0
        return self.GPA

    def register_for_course(self, course, grade):
        # Register a course for the student and update GPA
        self.courses_registered[course] = grade
        self.calculate_GPA()

    def to_dict(self):
        # Convert student object to a dictionary for JSON serialization
        return {
            "email": self.email,
            "names": self.names,
            "courses_registered": {course.name: grade for course, grade in self.courses_registered.items()},
            "GPA": self.GPA
        }

    @staticmethod
    def from_dict(data, courses):
        # Convert a dictionary back to a Student object
        courses_registered = {next(course for course in courses if course.name == name): grade 
                              for name, grade in data["courses_registered"].items()}
        return Student(data["email"], data["names"], courses_registered, data["GPA"])
