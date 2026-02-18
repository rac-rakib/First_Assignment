#import Class
from Course import Course
from Student import Student
from file_handling import save_student_to_file, show_all_students

# Create courses
python_course = Course("Python")
database_course = Course("Database")
math_course = Course("Math")

#Encapsulation (Private Data Protection)
student = Student("Rakib", 1, "secret123")
print("Password:", student.get_password())
#print(student.__password). Cannot Access

# Create student
student1 = Student("Rakib", 101, "pass123")

# Enroll courses
student1.enroll_course(python_course)
student1.enroll_course(database_course)
student1.enroll_course(math_course)

# Save to file
save_student_to_file(student1)

# Show all students from file
show_all_students()
