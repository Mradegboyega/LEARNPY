# Define a 'Human' class representing a generic human with basic information
class Human:
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_age(self):
        return self.age
    
    def get_details(self):
        return f"{self.get_full_name()} is {self.age} years old."

# Define a 'Student' class that inherits from the 'Human' class
class Student(Human):
    def __init__(self, first_name, last_name, age, grade, school) -> None:
        # Call the constructor of the parent class using super()
        super().__init__(first_name, last_name, age)

        self.grade = grade
        self.school = school

    def get_grade(self):
        return self.grade
    
    # Override the get_details method to provide student-specific details
    def get_details(self):
        return f"{self.get_full_name()} is {self.age} years old and is in grade {self.get_grade()} at {self.school}"

# Create an instance of the 'Student' class
glen = Student("Alex", "Smith", 15, 9, "High School")

# Print various details about the student
print(glen.get_full_name())
print(glen.get_age())
print(glen.get_details())
print(glen.get_grade())


# Define a 'Teacher' class that inherits from the 'Human' class
class Teacher(Human):
    def __init__(self, first_name, last_name, age, subject, school) -> None:
        # Call the constructor of the parent class using super()
        super().__init__(first_name, last_name, age)

        self.subject = subject
        self.school = school

    def get_subject(self):
        return self.subject
    
    # Override the get_details method to provide teacher-specific details
    def get_details(self):
        return f"{self.get_full_name()} is at {self.school}, {self.age} years old, and teaches {self.get_subject()}."

# Create an instance of the 'Teacher' class
shasha = Teacher("Shasha", "Jack", 25, "English", "High School")

# Print various details about the teacher
print(shasha.get_full_name())
print(shasha.get_age())
print(shasha.get_details())
print(shasha.get_subject())
