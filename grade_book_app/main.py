#!/usr/bin/env python3
# grade_book_app/main.py

from student import Student
from course import Course
from gradebook import GradeBook

def main():
    gradebook = GradeBook()

    while True:
        print("\nWELOCOME TO GRADE BOOK APPLICATION")
        print("Choose an action:")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for a course")
        print("4. Calculate ranking")
        print("5. Search by grade")
        print("6. Generate transcript")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            student = Student(email, names)
            gradebook.add_student(student)
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            course = Course(name, trimester, credits)
            gradebook.add_course(course)
        elif choice == '3':
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            student = next((s for s in gradebook.student_list if s.email == email), None)
            course = next((c for c in gradebook.course_list if c.name == course_name), None)
            if student and course:
                gradebook.register_student_for_course(student, course)
            else:
                print("Invalid student or course")
        elif choice == '4':
            gradebook.calculate_ranking()
        elif choice == '5':
            grade = input("Enter grade to search by: ")
            gradebook.search_by_grade(grade)
        elif choice == '6':
            email = input("Enter student email: ")
            student = next((s for s in gradebook.student_list if s.email == email), None)
            if student:
                gradebook.generate_transcript(student)
            else:
                print("Invalid student")
        elif choice == '0':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

