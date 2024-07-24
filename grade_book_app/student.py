#!/usr/bin/env python3
class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = {}
        self.GPA = 0.0

    def calculate_GPA(self):
        total_points = 0
        total_credits = 0
        for course, grade in self.courses_registered.items():
            total_points += grade * course.credits
            total_credits += course.credits
        self.GPA = total_points / total_credits if total_credits != 0 else 0.0
        return self.GPA

    def register_for_course(self, course, grade):
        self.courses_registered[course] = grade
