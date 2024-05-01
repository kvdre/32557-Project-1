from StudentController import StudentController
from AdminController import AdminController
from Database import Database

def main_menu():
    db = Database()
    while True:
        choice = input("Choose (A) Admin, (S) Student, (X) Exit: ").upper()
        if choice == 'A':
            admin_menu(db)
        elif choice == 'S':
            student_menu(db)
        elif choice == 'X':
            break
        else:
            print("Invalid choice.")

def student_menu(db):
    email = input("Email: ")
    password = input("Password: ")
    student = StudentController.login_student(db, email, password)
    if student:
        print("Login successful.")
        # Additional student menu actions
    else:
        print("Login failed or student not registered.")

def admin_menu(db):
    student_id = input("Enter student ID to remove: ")
    result = AdminController.remove_student(db, student_id)
    print(result)

if __name__ == "__main__":
    main_menu()
