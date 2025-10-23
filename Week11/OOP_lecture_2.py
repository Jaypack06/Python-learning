#Unit 1
# TODO: Create Person class with private _age
from unicodedata import name


class Person:
    def __init__(self, name, age):
        self.name = name # Public
        self._age = age # Private
    def get_age(self):
        # Return the private age
        return self._age
# Test:
person = Person("Bob", 25)
print(person.get_age()) # Should print 25
person._age = -5 # We shouldn't do this

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    def get_age(self):
        return self._age
    def set_age(self, new_age):
        if 0 <= new_age <= 150:
            self._age = new_age
            print(f"Age updated to {new_age}")
        else:
            print("Invalid age. Age must be between 0 and 150.")
# Test:
person = Person("Alice", 25)
person.set_age(30) # Should work
person.set_age(-5) # Should print error

# TODO: Store SSN privately, show only last 4 digits
class Person:
    def __init__(self, name, ssn):
        self.name = name
        # Store SSN privately
        self._ssn = ssn
    def get_masked_ssn(self):
        # Return like: ***-**-6789
        return "***-**-" + self._ssn[-4:]
    def verify_ssn(self, ssn_to_check):
        # Return True if matches stored SSN
        return ssn_to_check == self._ssn

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        # Calculate and return area
        return self.width * self.height
# Test:
rect = Rectangle(5, 3)
print(rect.area) # Should print 15 (no parentheses!)

# TODO: Extract domain from email
class Email:
    def __init__(self, address):
        self.address = address
    @property
    def username(self):
    # Return part before @
        return self.address.split("@")[0]
    @property
    def domain(self):
    # Return part after @
        return self.address.split("@")[1]
# Test:
email = Email("alice@gmail.com")
print(email.username) # alice
print(email.domain) # gmail.com

# TODO: Calculate age from birthdate
from datetime import datetime
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    @property
    def age(self):
        # Calculate age from birth_year
        return datetime.now().year - self.birth_year
# Use datetime.now().year
    @property
    def can_vote(self):
        # Return True if age >= 18
        return self.age >= 18
# Test:
person = Person("Bob", 2000)
print(f"Age: {person.age}")
print(f"Can vote: {person.can_vote}")