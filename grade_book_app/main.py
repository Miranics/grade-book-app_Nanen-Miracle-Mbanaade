#!/usr/bin/env python3
# grade_book_app/main.py

from gradebook import GradeBook

def main():
    gradebook = GradeBook()

    while True:
        print("\n______________________________________________"
            "\n-WELCOME TO MIRANICS; a gradebook application-"
              "  \n----------------------------------------------")
        print("Select an option:")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for a course")
        print("4. Calculate ranking")
        print("5. Search by grade")
        print("6. Generate transcript")
        print("7. View all students")
        print("8. Delete student")
        print("0. End program...")

        choice = input("SELECT> ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)
            print(f"Student {names} added successfully.")
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)
            print(f"Course {name} added successfully.")
        elif choice == '3':
            email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            try:
                gradebook.register_student_for_course(email, course_name, grade)
                print(f"Student {email} registered for course {course_name} with grade {grade}.")
            except ValueError as e:
                print(e)
        elif choice == '4':
            ranking = gradebook.calculate_ranking()
            print("Student Ranking:")
            for rank, student in enumerate(ranking, start=1):
                print(f"{rank}. {student.names} - GPA: {student.GPA:.2f}")
        elif choice == '5':
            grade = float(input("Enter grade to search by: "))
            students = gradebook.search_by_grade(grade)
            if students:
                print("Students with the specified grade:")
                for student in students:
                    print(f"{student.names} - {student.email}")
            else:
                print("No students found with the specified grade.")
        elif choice == '6':
            email = input("Enter student email: ")
            try:
                transcript = gradebook.generate_transcript(email)
                print("Transcript:")
                print(f"Name: {transcript['names']}")
                print(f"Email: {transcript['email']}")
                print(f"GPA: {transcript['GPA']:.2f}")
                print("Courses:")
                for course, grade in transcript['courses']:
                    print(f"Course: {course}, Grade: {grade}")
            except ValueError as e:
                print(e)
        elif choice == '7':
            students = gradebook.view_all_students()
            print("Registered Students:")
            for student in students:
                print(f"Name: {student.names}, Email: {student.email}, GPA: {student.GPA:.2f}")
        elif choice == '8':
            email = input("Enter student email to delete: ")
            gradebook.delete_student(email)
            print(f"Student with email {email} has been deleted.")
        elif choice == '0':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
