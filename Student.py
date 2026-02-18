#Create Student Class
class Student:
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self.__password = password   # private variable (Encapsulation)
        self.courses = []            # enrolled courses list

    def enroll_course(self, course):
        self.courses.append(course.course_name)

    # Getter method (To view the password)
    def get_password(self):
        return self.__password