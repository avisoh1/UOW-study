class Subject:
    def __init__(self, code, name):
        self.__code = code
        self.__name = name
        self.__teacher = None
        self.__students = []

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def get_teacher(self):
        return self.__teacher

    def get_students(self):
        return self.__students

    def set_teacher(self, teacher):
        self.__teacher = teacher
        teacher.add_subject(self)  # self is a subject object

    def add_student(self, student):
        self.__students.append(student)
        student.add_subject(self)

    def remove_student(self, student):
        self.__students.remove(student)
        student.remove_subject(self)

    def __str__(self):
        teacher_name = self.__teacher.get_name() if self.__teacher else "No teacher yet"
        student_names = [s.get_name() for s in self.__students]
        students_str = ", ".join(student_names) if student_names else "No students enrolled"
        return f"Subject Code: {self.__code}\nSubject Name: {self.__name}\nTeacher: {teacher_name}\nEnrolled Students: {students_str}"

class Teacher:
    def __init__(self, staff_id, name):
        self.__staff_id = staff_id
        self.__name = name
        self.__subjects = []

    def get_staff_id(self):
        return self.__staff_id

    def get_name(self):
        return self.__name

    def get_subjects(self):
        return self.__subjects

    def add_subject(self, subject):
        self.__subjects.append(subject)

    def remove_subject(self, subject):
        self.__subjects.remove(subject)

    def __str__(self):
        subject_names = [s.get_name() for s in self.__subjects]
        subjects_str = ", ".join(subject_names) if subject_names else "Not assign any yet"
        return f"Teacher ID: {self.__staff_id}\nTeacher Name: {self.__name}\nTeaching Subjects: {subjects_str}"


class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name
        self.__subjects = []

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_subjects(self):
        return self.__subjects

    def add_subject(self, subject):
        self.__subjects.append(subject)

    def remove_subject(self, subject):
        self.__subjects.remove(subject)

    def __str__(self):
        subject_names = [s.get_name() for s in self.__subjects]
        subjects_str = ", ".join(subject_names) if subject_names else "No subjects enrolled"
        return f"Student ID: {self.__student_id}\nStudent Name: {self.__name}\nEnrolled Subjects: {subjects_str}"


class EnrollmentSystem:
    def __init__(self):
        self.__subjects = []
        self.__teachers = []
        self.__students = []

    def create_subject(self, code, name):
        subject = Subject(code, name)
        self.__subjects.append(subject)
        return subject

    def create_teacher(self, staff_id, name):
        teacher = Teacher(staff_id, name)
        self.__teachers.append(teacher)
        return teacher

    def create_student(self, student_id, name):
        student = Student(student_id, name)
        self.__students.append(student)
        return student

    def find_subject_by_code(self, code):
        for s in self.__subjects:
            if s.get_code() == code:
                return s
        return None

    def find_student_by_id(self, student_id):
        for s in self.__students:
            if s.get_student_id() == student_id:
                return s
        return None

if __name__ == '__main__':
    #testing cases
    # Create an instance of the EnrollmentSystem
    enrollment_system = EnrollmentSystem()

    # Create subjects
    math_subject = enrollment_system.create_subject("MATH101", "Mathematics")
    physics_subject = enrollment_system.create_subject("PHY201", "Physics")
    chemistry_subject = enrollment_system.create_subject("CHEM301", "Chemistry")

    # Create teachers
    math_teacher = enrollment_system.create_teacher("T001", "Maths Smith")
    physics_teacher = enrollment_system.create_teacher("T002", "Phy Doe")

    # Create students
    student1 = enrollment_system.create_student("S001", "Alice Johnson")
    student2 = enrollment_system.create_student("S002", "Bob Anderson")
    student3 = enrollment_system.create_student("S003", "Carol Wilson")

    # Assign teachers to subjects
    math_subject.set_teacher(math_teacher)
    physics_subject.set_teacher(physics_teacher)

    # Enroll students in subjects
    math_subject.add_student(student1)
    math_subject.add_student(student2)
    physics_subject.add_student(student2)
    chemistry_subject.add_student(student3)

    # Test printing subject details
    print(math_subject)
    print(physics_subject)
    print(chemistry_subject)
    print("======================")
    # Test printing teacher details
    print(math_teacher)
    print(physics_teacher)
    print("======================")
    # Test printing student details
    print(student1)
    print(student2)
    print(student3)
    print("======================")
  
    # Search for a subject by code
    subject_code = "MATH101"
    subject = enrollment_system.find_subject_by_code(subject_code)
    if subject:
        print(f"Subject found: {subject.get_name()}")
        #print(subject)
    else:
        print("Subject not found.")

    # Search for a student by ID
    student_id = "S002"
    student = enrollment_system.find_student_by_id(student_id)
    if student:
        print(f"Student found: {student.get_name()}")
        enrolled_subjects = student.get_subjects()
        print("Enrolled Subjects:")
        for subject in enrolled_subjects:
            print(subject.get_name())
        #print(student)
    else:
        print("Student not found.")                    
