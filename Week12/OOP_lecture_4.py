# TODO: Different shapes, same draw() method
class Shape:
	def __init__(self, color):
		self.color = color
	def draw(self):
		pass
class Circle(Shape):
	def draw(self):
		# Return "Drawing a [color] circle"
		return f"Drawing a {self.color} circle"
class Square(Shape):
	def draw(self):
		# Return "Drawing a [color] square"
		return f"Drawing a {self.color} square"
# Test:
shapes = [Circle("red"), Square("blue"), Circle("green")]
for shape in shapes:
	print(shape.draw())


class Payment:
	def __init__(self, amount):
		self.amount = amount
	def process(self):
		pass
class CreditCard(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    def process(self):
        # Return "Processing $X via credit card ending in [last 4 digits]"
        return f"Processing ${self.amount} via credit card ending in {self.card_number[-4:]}"
class PayPal(Payment):
    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email
    def process(self):
        # Return "Processing $X via PayPal account [email]"
        return f"Processing ${self.amount} via PayPal account {self.email}"
# Process different payments the same way
payments = [CreditCard(100, "1234"), PayPal(200, "user@example.com")]
for payment in payments:
    print(payment.process())
    
    
class FileHandler:
	def __init__(self, filename):
		self.filename = filename
		self.data = None
	def save(self, content):
		raise NotImplementedError("save must be implemented by subclasses")
	def load(self):
		raise NotImplementedError("load must be implemented by subclasses")
class TextFile(FileHandler):
	def save(self, content):
		# Print "Saving text to [filename].txt"
		print(f"Saving text to {self.filename}.txt")
		self.data = content
	def load(self):
		# Return the saved data
		return self.data
class JsonFile(FileHandler):
	def save(self, content):
		# Print "Converting to JSON and saving to [filename].json"
		import json
		print(f"Converting to JSON and saving to {self.filename}.json")
		self.data = json.dumps(content)
	def load(self):
		import json
		try:
			return json.loads(self.data)
		except Exception:
			return self.data
class CsvFile(FileHandler):
	# Implement CSV saving/loading
	def save(self, content):
		# content expected as list of rows (lists)
		print(f"Saving CSV to {self.filename}.csv")
		lines = []
		for row in content:
			lines.append(','.join(map(str, row)))
		self.data = "\n".join(lines)
	def load(self):
		if not self.data:
			return []
		return [row.split(',') for row in self.data.splitlines()]
# Use any file type the same way!

from abc import ABC, abstractmethod
# TODO: Create abstract Vehicle class
class Vehicle(ABC):
	def __init__(self, brand):
		self.brand = brand

	@abstractmethod
	def start(self):
		# Force all vehicles to have start()
		pass

class Car(Vehicle):
	def start(self):
		# Return "Car engine starting..."
		return "Car engine starting..."

# Test:
car = Car("Toyota")
print(car.start())
# vehicle = Vehicle("Generic") # Should error! (cannot instantiate abstract class)

class DatabaseConnection(ABC):
	def __init__(self, host):
		self.host = host
		self.connected = False

	@abstractmethod
	def connect(self):
		"""Establish the connection."""
		raise NotImplementedError

	@abstractmethod
	def disconnect(self):
		"""Close the connection."""
		raise NotImplementedError

	@abstractmethod
	def execute_query(self, query):
		"""Execute a query and return results."""
		raise NotImplementedError

class MySQLConnection(DatabaseConnection):
	def connect(self):
		self.connected = True
		print(f"Connecting to MySQL at {self.host}")
		return True

	def disconnect(self):
		self.connected = False
		print(f"Disconnecting from MySQL at {self.host}")
		return True

	def execute_query(self, query):
		if not self.connected:
			raise RuntimeError("Not connected to MySQL")
		print(f"Executing MySQL query: {query}")
		# Return a dummy result for demonstration
		return [{"result": "mysql_dummy"}]

class PostgresConnection(DatabaseConnection):
	def connect(self):
		self.connected = True
		print(f"Connecting to Postgres at {self.host}")
		return True

	def disconnect(self):
		self.connected = False
		print(f"Disconnecting from Postgres at {self.host}")
		return True

	def execute_query(self, query):
		if not self.connected:
			raise RuntimeError("Not connected to Postgres")
		print(f"Executing Postgres query: {query}")
		# Return a dummy result for demonstration
		return [{"result": "postgres_dummy"}]


class Plugin(ABC):
	def __init__(self, name, version):
		self.name = name
		self.version = version
		self.enabled = False

	@abstractmethod
	def activate(self):
		"""Called when plugin is enabled"""
		raise NotImplementedError

	@abstractmethod
	def deactivate(self):
		"""Called when plugin is disabled"""
		raise NotImplementedError

	@abstractmethod
	def process(self, data):
		"""Main plugin functionality"""
		raise NotImplementedError

# Create different plugin types
class SpellChecker(Plugin):
	# Implement spell checking
	def __init__(self, name="SpellChecker", version="1.0"):
		super().__init__(name, version)

	def activate(self):
		self.enabled = True
		return f"{self.name} v{self.version} activated"

	def deactivate(self):
		self.enabled = False
		return f"{self.name} deactivated"

	def process(self, data):
		# naive implementation: return words that look "misspelled" (dummy logic)
		if not isinstance(data, str):
			return []
		words = data.split()
		# Dummy rule: consider words longer than 12 characters as misspelled
		return [w for w in words if len(w) > 12]

class AutoSave(Plugin):
	# Implement auto-saving
	def __init__(self, name="AutoSave", version="1.0", interval=60):
		super().__init__(name, version)
		self.interval = interval

	def activate(self):
		self.enabled = True
		return f"{self.name} activated with interval {self.interval}s"

	def deactivate(self):
		self.enabled = False
		return f"{self.name} deactivated"

	def process(self, data):
		# Dummy autosave: return a summary indicating saved status
		return {"saved": True, "length": len(data) if hasattr(data, "__len__") else None}

# TODO: Create objects with compatible methods
class Calculator:
	def compute(self, x, y):
		return x + y

class ScientificCalculator: # No inheritance!
	def compute(self, x, y):
		# Return x * y instead
		return x * y

def process_numbers(processor, a, b):
	# Works with anything that has compute()
	result = processor.compute(a, b)
	print(f"Result: {result}")

# Test both calculators
if __name__ == "__main__":
	calc = Calculator()
	sci = ScientificCalculator()
	process_numbers(calc, 2, 3)
	process_numbers(sci, 2, 3)
 
# TODO: Make custom iterable class
class Countdown:
	def __init__(self, start):
		self.start = start
		self.current = start
	def __iter__(self):
		# Return self
		return self
	def __next__(self):
		# Count down to 0
		# Raise StopIteration when done
		if self.current < 0:
			raise StopIteration
		value = self.current
		self.current -= 1
		return value
# Test:
for num in Countdown(5):
	print(num) # Should print 5, 4, 3, 2, 1, 0