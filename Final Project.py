class Course:
    course_id = 0

    def __init__(self, name, level):
        Course.course_id += 1
        self.id = Course.course_id
        self.name = name
        self.level = level


class Student:
    student_id = 0

    def __init__(self, name, level):
        Student.student_id += 1
        self.id = Student.student_id
        self.name = name
        self.level = level
        self.courses = []

    def add_course(self, course):
        if self.level == course.level:
            self.courses.append(course)
            print("Course added successfully.")
        else:
            print("Course level is not compatible with student level.")

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print("Courses:")
        for i in self.courses:
            print(f"{i.name}")


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, name, level):
        student = Student(name, level)
        self.students.append(student)
        print("Student saved successfully.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")

    def edit_student(self, student_id, new_name, new_level):
        for student in self.students:
            if student.id == student_id:
                student.name = new_name
                student.level = new_level
                print("Student edited successfully.")
                return
        print("Student not found.")

    def display_all_students(self):
        for student in self.students:
            student.display_details()

    def add_course(self, name, level):
        course = Course(name, level)
        self.courses.append(course)
        print("Course created successfully.")

    def add_course_to_student(self, student_id, course_id):
        student_found = False
        course_found = False
        for i in self.students:
            if i.id == student_id:
                student_found = True
                for j in self.courses:
                    if j.id == course_id:
                        course_found = True
                        student.add_course(course)
                        return
                break
        if not student_found:
            print("Student not found.")
        elif not course_found:
            print("Course not found.")

school = School()

while True:
    print("1. Add New Student")
    print("2. Remove the Student")
    print("3. Edit Student")
    print("4. Display all students")
    print("5. Create a new Course")
    print("6. Add Course to student")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        level = ""
        while level not in ["A", "B", "C"]:
            level = input("Enter student level (A-B-C): ")
        school.add_student(name, level)

    elif choice == "2":
        student_id = int(input("Enter student id: "))
        school.remove_student(student_id)

    elif choice == "3":
        student_id = int(input("Enter student id: "))
        new_name = input("Enter new name: ")
        new_level = ""
        while new_level not in ["A", "B", "C"]:
            new_level = input("Enter new level (A-B-C): ")
        school.edit_student(student_id, new_name, new_level)

    elif choice == "4":
        school.display_all_students()

    elif choice == "5":
        name = input("Enter course name: ")
        level = ""
        while level not in ["A", "B", "C"]:
            level = input("Enter course level (A-B-C): ")
        school.add_course(name, level)

    elif choice == "6":
        student_id = int(input("Enter student id: "))
        course_id = int(input("Enter course id: "))
        school.add_course_to_student(student_id, course_id)

    elif choice == "0":
        break

    else:
        print("Invalid choice.")