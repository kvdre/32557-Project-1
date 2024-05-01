import random

class Student:
    def __init__(self, name, email, password):
        self.id = str(random.randint(1, 999999)).zfill(6)
        self.name = name
        self.email = email
        self.password = password
        self.subjects = []  # subjects object list

    def add_subject(self, subject):
        if len(self.subjects) < 4:
            self.subjects.append(subject)
            return True
        return False

    def remove_subject(self, subject_id):
        for subject in self.subjects:
            if subject.id == subject_id:
                self.subjects.remove(subject)
                return True
        return False
