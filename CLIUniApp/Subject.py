import random

class Subject:
    def __init__(self):
        self.id = str(random.randint(1, 999)).zfill(3)
        self.mark = random.randint(25, 100)
        self.grade = self.determine_grade()

    def determine_grade(self):
        if self.mark >= 85:
            return 'HD'
        elif self.mark >= 75:
            return 'D'
        elif self.mark >= 60:
            return 'C'
        elif self.mark >= 50:
            return 'P'
        else:
            return 'Z'
