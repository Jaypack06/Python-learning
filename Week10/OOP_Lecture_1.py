#unit 1
# TODO: Create a Book class with title and author
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
# Test it:
my_book = Book("Python Basics", "Jane Doe")
print(my_book.title) # Should print: Python Basics

# TODO: Add display_info() method to Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

# TODO: Create multiple books and store in a list
class Book:
# Your Book class here
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

# Create a library (list of books)
library = []
# Add at least 3 books to library
library.append(Book("Python Basics", "Jane Doe"))
library.append(Book("Advanced Python", "John Smith"))
library.append(Book("Python OOP", "Alice Johnson"))
# Print all book titles in library
for book in library:
    book.display_info()
#Unit 2
# TODO: Create Car with make, model, year
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
# Test:
my_car = Car("Toyota", "Camry", 2020)
print(f"{my_car.year} {my_car.make} {my_car.model}")

# TODO: Add mileage and drive() method
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
    def drive(self, miles):
        self.mileage += miles
        print(f"Total mileage: {self.mileage}")
# Test:
my_car = Car("Honda", "Civic", 2019)
my_car.drive(100)
print(f"{my_car.year} {my_car.make} {my_car.model} with {my_car.mileage} miles")

# TODO: Add fuel tank and consumption
class Car:
    def __init__(self, make, model, year, mpg):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0
        self.fuel_tank = 0
        self.mpg = mpg
    def drive(self, miles):
        fuel_needed = miles / self.mpg
        if fuel_needed > self.fuel_tank:
            print("Not enough fuel!")
            return
        self.mileage += miles
        self.fuel_tank -= fuel_needed
#test:
my_car = Car("Ford", "Focus", 2018, 30)
my_car.fuel_tank = 10 # gallons
my_car.drive(100)
print(f"{my_car.year} {my_car.make} {my_car.model} with {my_car.mileage} miles and gets {my_car.mpg} MPG")
#Unit 3
# TODO: Create Teacher class that holds students
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []
# Add method to add a student
    def add_student(self, student_name):
        self.students.append(student_name)
# Test:
teacher = Teacher("Mr. Johnson")
teacher.add_student("Alice")
teacher.add_student("Bob")
print(teacher.students)

# TODO: Add remove_student method
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student_name):
        self.students.append(student_name)

    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)  # Remove if found
# Test:
teacher = Teacher("Ms. Smith")  
teacher.add_student("Alice")
teacher.add_student("Bob")
teacher.remove_student("Alice")
print(teacher.students)  # Should print ['Bob']


# TODO: Track grades for each student
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = {} # Dictionary: name -> grade
    def add_student(self, name, initial_grade=0):
        self.students[name] = initial_grade
    def grade_student(self, name, grade):
        # Update grade if student exists
        if name in self.students:
            self.students[name] = grade
    def class_average(self):
        # Calculate and return average grade
        if not self.students:
            return 0
        return sum(self.students.values()) / len(self.students)
#test:
teacher = Teacher("Dr. Brown")
teacher.add_student("Alice", 85)
teacher.add_student("Bob", 90)
teacher.grade_student("Alice", 95)
print(teacher.class_average())  # Should print average of Alice and Bob's grades    
#Unit 4
class Book:
    def __init__(self, title):
        self.title = title
    def __del__(self):
        print(f"Book '{self.title}' is being deleted.")
my_book = Book("Python Fun")
print(my_book.title)
del my_book