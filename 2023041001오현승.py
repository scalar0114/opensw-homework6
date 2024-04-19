class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score

    def calculate_total_average(self):
        total = self.english_score + self.c_score + self.python_score
        average = total / 3
        return total, average

    def calculate_grade(self):
        _, average = self.calculate_total_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

class StudentManager:
    def __init__(self):
        self.students = []

    def input_student(self):
        student_id = input("ID: ")
        name = input("name: ")
        english_score = int(input("En score: "))
        c_score = int(input("C score: "))
        python_score = int(input("Python score: "))
        print("Student added\n")
        self.students.append(Student(student_id, name, english_score, c_score, python_score))

    def calculate_rank(self):
        self.students.sort(key=lambda x: x.calculate_total_average()[0], reverse=True)
        for i, student in enumerate(self.students):
            student.rank = i + 1

    def print_students(self):
        for student in self.students:
            total, average = student.calculate_total_average()
            grade = student.calculate_grade()
            print(f"ID: {student.student_id}, Name: {student.name}, Total: {total}, Average: {average}, Grade: {grade}, Rank: {student.rank}\n")

    def delete_student(self):
        student_id = input("ID to delete: ")
        self.students = [student for student in self.students if student.student_id != student_id]
        print("Student deleted\n")

    def search_student(self):
        search_id = input("ID or name for search: ")
        for student in self.students:
            if student.student_id == search_id or student.name == search_id:
                return student
        return None

    def sort_students(self):
        print("Sorting complete\n")
        self.students.sort(key=lambda x: x.calculate_total_average()[0], reverse=True)

    def count_students_above_80(self):
        count = 0
        for student in self.students:
            if student.calculate_total_average()[1] >= 80:
                count += 1
        return count

def main():
    manager = StudentManager()
    while True:
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Sort")
        print("5. Print")
        print("6. Number of students with average above 80:")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            manager.input_student()
        elif choice == 2:
            manager.delete_student()
        elif choice == 3:
            student = manager.search_student()
            if student:
                print(f"ID: {student.student_id}, Name: {student.name}, En: {student.english_score}, C: {student.c_score}, Python: {student.python_score}\n")
            else:
                print("No student found\n")
        elif choice == 4:
            manager.sort_students()
        elif choice == 5:
            manager.calculate_rank()
            manager.print_students()
        elif choice == 6:
            count = manager.count_students_above_80()
            print(f"Number of students with average above 80: {count}\n")
        elif choice == 7:
            break
        else:
            print("Invalid choice\n")

main()