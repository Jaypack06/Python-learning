
from datetime import datetime
# TODO: Create Person with from_birth_year class method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_birth_year(cls, name, birth_year):
    # Calculate age from birth_year
        # Use: from datetime import datetime
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age)
# Test:
person = Person.from_birth_year("Alice", 2000)
print(f"{person.name} is {person.age} years old")

# TODO: Load configuration from different sources
class Config:
    def __init__(self, host, port, debug):
        self.host = host
        self.port = port
        self.debug = debug
    @classmethod
    def from_json_string(cls, json_str):
        # Parse JSON-like string
        # "{'host': 'localhost', 'port': 8080, 'debug': true}"
        return cls(**eval(json_str.replace("true", "True").replace("false", "False")))
    @classmethod
    def default_config(cls):
        # Return config with default values
        # host='localhost', port=8080, debug=False
        return cls("localhost", 8080, False)
# Test different config sources
default_config = Config.default_config()
print(f"Default config: {default_config.host}:{default_config.port}")
json_config = Config.from_json_string("{'host': 'localhost', 'port': 8080, 'debug': True}")
print(f"JSON config: {json_config.host}:{json_config.port}")

# TODO: Create model that loads from database
class User:
    user_count = 0 # Track total users
    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1
    @classmethod
    def from_database_row(cls, row):
# row is a tuple like ('alice', 'alice@email.com')
        return cls(row[0], row[1])
    @classmethod
    def create_guest(cls):
# Create guest user with generated name
# Like "guest_001", "guest_002", etc.
        guest_name = f"guest_{User.user_count + 1:03d}"
        return cls(guest_name, f"{guest_name}@example.com")
    @classmethod
    def get_total_users(cls):
# Return total user count
        return User.user_count
# Test user creation
user1 = User.from_database_row(('alice', 'alice@example.com'))
user2 = User.create_guest()
print(f"Total users: {User.get_total_users()}")

# TODO: Create static email validation
class EmailValidator:
    @staticmethod
    def is_valid_email(email):
# Check: has @
# Check: has . after @
# Return True/False
        return "@" in email and "." in email.split("@")[1]
    @staticmethod
    def get_domain(email):
# Return part after @
# Return None if invalid
        if "@" in email:
            return email.split("@")[1]
        return None     
# Test:
print(EmailValidator.is_valid_email("test@gmail.com"))
print(EmailValidator.get_domain("user@example.org"))

# TODO: File helper static methods
class FileHelper:
    @staticmethod
    def get_extension(filename):
# Return file extension (after last .)
# "document.pdf" → "pdf"
        return filename.split(".")[-1]
    @staticmethod
    def is_image(filename):
# Check if extension is jpg, png, gif
        return FileHelper.get_extension(filename).lower() in ["jpg", "png", "gif"]
    @staticmethod
    def make_safe_filename(text):
# Replace spaces with underscore
# Remove special characters
        return text.replace(" ", "_").replace(".", "").replace(",", "")
# Test with various filenames
print(FileHelper.get_extension("document.pdf"))
print(FileHelper.is_image("photo.jpg"))
print(FileHelper.make_safe_filename("My Document, 2023.pdf"))