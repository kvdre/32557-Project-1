from Database import Database
from Student import Student

class StudentController:
    @staticmethod
    def register_student(db, name, email, password):
        if any(s.email == email for s in db.data):
            return "Student already registered."
        student = Student(name, email, password)
        db.data.append(student)
        db.save_data()
        return "Registration successful."

    @staticmethod
    def login_student(db, email, password):
        for student in db.data:
            if student.email == email and student.password == password:
                return student
        return None
