# Save Data into File
def save_student_to_file(student):
    with open("students.txt", "a") as file:
        courses = ",".join(student.courses)
        file.write(f"Name: {student.name}, Roll: {student.roll}, Courses: {courses}\n")

# Read Data
def show_all_students():
    try:
        with open("students.txt", "r") as file:
            print("All Enrolled Students:\n")
            for line in file:
                print(line.strip())
    except Exception as error:
        print(f"Oops! An error occurred: {error}")