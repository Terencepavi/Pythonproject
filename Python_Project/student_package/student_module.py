class Student:
    school_name = None
    scholl_adress = None

    def __init__(self, student_id, student_name=None, student_mailid=None, student_percentage=None):
        self.student_id = student_id
        self.student_name = student_name
        self.student_mailid = student_mailid
        self.student_percentage = student_percentage

    def print_grade(self):
        if self.student_percentage > 100 or self.student_percentage < 0:
            print("Invalid input")
        elif self.student_percentage >= 90:
             print("Grade A")
        elif self.student_percentage >= 80 and self.student_percentage <= 89:
            print("Grade B")
        elif self.student_percentage >= 60 and self.student_percentage <= 79:
            print("Grade C")
        else:
            print("Failed, Please re-attempt")
    @property
    def get_student_name(self):
        return self.student_name
    @property
    def get_name_with_percentage(self):
        return ("Hi "+self.student_name+"-your percentage is "+str(self.student_percentage)+"%")