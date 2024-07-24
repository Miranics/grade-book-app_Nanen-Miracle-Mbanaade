#!/usr/bin/env python3
# grade_book_app/main.py

from grade_book_app.gradebook import GradeBook


def main():
    gradebook = GradeBook()

    while True:
        print("\nGrade Book Application")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            email = input("Enter student email: ")
            first_name = input("Enter student first name: ")
            last_name = input("Enter student last name: ")
            gradebook.add_student(email, first_name, last_name)
            print("Student added successfully!")

        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
            print("Course added successfully!")

        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            gradebook.register_student_for_course(student_email, course_name)
            print("Student registered for course successfully!")

        elif choice == '4':
            gradebook.calculate_GPA()
            print("GPA calculated for all students.")

        elif choice == '5':
            gradebook.calculate_ranking()
            print("Student ranking displayed.")

        elif choice == '6':
            min_grade = float(input("Enter minimum grade: "))
            max_grade = float(input("Enter maximum grade: "))
            gradebook.search_by_grade(min_grade, max_grade)

        elif choice == '7':
            student_email = input("Enter student email: ")
            gradebook.generate_transcript(student_email)

        elif choice == '8':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
