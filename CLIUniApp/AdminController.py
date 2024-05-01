from Database import Database

class AdminController:
    @staticmethod
    def remove_student(db, student_id):
        for student in db.data:
            if student.id == student_id:
                db.data.remove(student)
                db.save_data()
                return "Student removed."
        return "Student not found."
