# Part 1: Class Definition
class Student:
    def __init__(self, name, email, grades=None):
        self.name = name
        self.email = email
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        """Add a single grade to the list of grades."""
        self.grades.append(grade)

    def average_grade(self):
        """Return the average of all grades."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        """Print the student's name, email, and grades."""
        print(f"Name: {self.name}, Email: {self.email}, Grades: {self.grades}")

# Part 2: Working with Objects
# Create three student objects
student1 = Student("Chris", "chris@example.com", [85, 90, 78])
student2 = Student("Ryan", "ryan@example.com", [92, 88, 84])
student3 = Student("Craig", "craig@example.com", [75, 80, 82])

# Add two new grades to each student
student1.add_grade(88)
student1.add_grade(91)

student2.add_grade(79)
student2.add_grade(85)

student3.add_grade(83)
student3.add_grade(77)

# Print each student's info and average grade
for student in [student1, student2, student3]:
    student.display_info()
    print(f"Average Grade: {student.average_grade():.2f}\n")

# Part 3: Dictionary & Set Integration
# Create a dictionary mapping emails to student objects
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

def get_student_by_email(email):
    """Retrieve a student object by email from the dictionary."""
    return student_dict.get(email, None)

# Create a set of all unique grades across all students
all_grades = set()
for student in student_dict.values():
    all_grades.update(student.grades)

print("Unique grades across all students:", all_grades)

# Part 4: Tuple Practice
# Add a method to return grades as a tuple
def grades_tuple(self):
    """Return the grades as a tuple."""
    return tuple(self.grades)

# Add the new method to the class
Student.grades_tuple = grades_tuple

# Demonstrate that tuples are immutable
try:
    student1_tuple = student1.grades_tuple()
    # Attempt to change a value (will raise an error)
    student1_tuple[0] = 100
except TypeError:
    print("Tuples are immutable; you cannot modify them.")

# Part 5: List Operations
# Remove the last grade from each student's grades list
for student in student_dict.values():
    if student.grades:
        student.grades.pop()

# Print the first and last grade for each student and the number of grades
for student in student_dict.values():
    if student.grades:
        first_grade = student.grades[0]
        last_grade = student.grades[-1]
        num_grades = len(student.grades)
        print(f"{student.name}: First grade: {first_grade}, Last grade: {last_grade}, Number of grades: {num_grades}")

