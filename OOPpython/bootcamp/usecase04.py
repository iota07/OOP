import random


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class StudentGroup:
    def __init__(self, students):
        self.students = students

    def calculate_average_score(self):
        total_score = sum(student.grade for student in self.students)
        average_score = total_score / len(self.students)
        return average_score

    def move_student(self, student, target_group):
        if student in self.students:
            self.students.remove(student)
            target_group.students.append(student)
            print(f"{student.name} moved to the other group.")
        else:
            print(f"{student.name} is not in this group.")

    def display_all_grades(self):
        print(f"Grades for this group:")
        for student in self.students:
            print(f"{student.name}: {student.grade}")

    def move_top_student(self, target_group):
        top_student = max(self.students, key=lambda student: student.grade)
        self.move_student(top_student, target_group)


# Generate two groups of 10 students each
def generate_students(num_students):
    students = []
    for i in range(num_students):
        name = f"Student_{i+1}"
        grade = random.randint(0, 100)
        students.append(Student(name, grade))
    return students


students_group1 = generate_students(10)
students_group2 = generate_students(10)

# Create student groups
group1 = StudentGroup(students_group1)
group2 = StudentGroup(students_group2)

# Display all grades before moving
group1.display_all_grades()
group2.display_all_grades()

# Display average scores before moving
print(f"\nGroup 1 Average Score: {group1.calculate_average_score()}")
print(f"Group 2 Average Score: {group2.calculate_average_score()}")

# Move the top student from group 2 to group 1
group2.move_top_student(group1)

# Display all grades after moving
print("\nAfter moving:")
group1.display_all_grades()
group2.display_all_grades()

# Display average scores after moving
print(f"\nGroup 1 Average Score: {group1.calculate_average_score()}")
print(f"Group 2 Average Score: {group2.calculate_average_score()}")
