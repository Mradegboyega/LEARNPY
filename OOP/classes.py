# Define a Person class
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age}")

# Create instances of the Person class
Oluwatoyin = Person("Oluwatoyin", 29)
Michelle = Person("Michelle", 2)

# Call the say_hello method for each person
Oluwatoyin.say_hello()
Michelle.say_hello()

# Define a User class
class User:
    def __init__(self, first_name, last_name, user_name, password) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_password(self):
        return self.password

    def validate_password(self, password):
        return self.password == password

# Create instances of the User class
Oluwatoyin = User("Oluwatoyin", "Ademola", "missyt", "password")
Michelle = User("Michelle", "Ademola", "missmichelle", "password")

# Call methods on the User instances and print the results
print(Oluwatoyin.get_full_name())
print(Oluwatoyin.get_password())
print(Michelle.get_full_name())
print(Michelle.get_password())



class Student:

    num_of_students = 0

    def __init__(self, first_name, last_name, age, grade) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade  # Fix: Correct the assignment of grade

        Student.num_of_students += 1

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_grade(self):
        return self.grade

    def get_student_details(self):
        return f"{self.get_full_name()} is {self.age} years old. My grade is {self.get_grade()}"
    
# Create instances of the Student class
craig = Student("Craig", "Ayo", 20, 7)
toby = Student("Toby", "Geo", 28, 17)

# Print the total number of students using the class variable
print(Student.num_of_students)

# Accessing the class variable through an instance (not recommended, use the class name)
print(toby.num_of_students)  # Note: It's better to use Student.num_of_students
