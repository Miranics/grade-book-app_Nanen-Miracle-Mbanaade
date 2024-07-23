class Student:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.courses_registered = []  # List of courses registered
        self.grades = {}  # Dictionary: Course -> Grade

    def calculate_GPA(self):
        if not self.courses_registered:
            return 0.0  # No courses, GPA is 0.0

        total_credits, total_quality_points = 0, 0
        for course, grade in self.grades.items():
            total_credits += course.credits
            total_quality_points += grade * course.credits
        return total_quality_points / total_credits if total_credits else 0.0

    def register_for_course(self, course):
        self.courses_registered.append(course)
        self.grades[course] = None  # Initialize grade as None

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} ({self.email})"
