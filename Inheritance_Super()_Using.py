# Define the base class 'Person'
class Person:
    # Initialize with name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Define a subclass 'Student' that inherits from 'Person'
class Student(Person):
    # Initialize with name, age, and faculty
    def __init__(self, name, age, faculty):
        # Call the parent class's __init__ method to initialize name and age
        super().__init__(name, age)
        # Initialize the faculty attribute specific to 'Student'
        self.faculty = faculty

# Create an instance of 'Student' with name "Alice", age 20, and faculty "Engineering"
student = Student("Alice", 20, "Engineering")

# Print the name, age, and faculty of the student
print(f"Name: {student.name}")  # Output: Name: Alice
print(f"Age: {student.age}")    # Output: Age: 20
print(f"Faculty: {student.faculty}")  # Output: Faculty: Engineering
