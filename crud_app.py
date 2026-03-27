# crud_app.py

students = []


def create_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age
    }

    students.append(student)
    print("Student added successfully!\n")


def read_students():
    if not students:
        print("No student records found.\n")
        return

    print("\nStudent Records:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")
    print()


def update_student():
    student_id = input("Enter student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    student_id = input("Enter student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Create Student")
        print("2. Read Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_student()
        elif choice == "2":
            read_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.\n")


menu()
