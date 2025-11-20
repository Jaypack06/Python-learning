from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    def describe(self):
        return f"This is a {self.__class__.__name__}."
    
    @staticmethod
    def validate_positive(value):
        if value <= 0:
            raise ValueError("Value must be positive.")
    
class Circle(Shape):
    def __init__(self, radius):
        self.validate_positive(radius)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.validate_positive(width)
        self.validate_positive(height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.validate_positive(a)
        self.validate_positive(b)
        self.validate_positive(c)
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides.")
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c
    
class shapecollection:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape):
        if not isinstance(shape, Shape):
            raise TypeError("Only Shape instances can be added.")
        self.shapes.append(shape)

    def total_area(self):
        return sum(shape.area() for shape in self.shapes)

    def total_perimeter(self):
        return sum(shape.perimeter() for shape in self.shapes)
    
if __name__ == "__main__":
    # Create shapes
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)
    # Test individual shapes
    print("Individual Shapes:")
    for shape in [circle, rectangle, triangle]:
        print(f" {shape.describe()}")
        print(f" Area: {shape.area():.2f}")
        print(f" Perimeter: {shape.perimeter():.2f}")
    # Test collection (polymorphism!)
    collection = shapecollection()
    collection.add_shape(circle)
    collection.add_shape(rectangle)
    collection.add_shape(triangle)
    print(f"\nCollection Totals:")
    print(f" Total Area: {collection.total_area():.2f}")
    print(f" Total Perimeter: {collection.total_perimeter():.2f}")
    # Test validation
    print("\nTesting validation:")
    try:
        bad_circle = Circle(-5)
    except:
        print(" Correctly rejected negative radius")

"""---------------------------------------------------------------------------"""

class Pizza:
    price_list = {'small' : 10, 'medium' : 15, 'large' : 20}
    topping_price = 2

    def __init__(self, size, toppings):
        if size not in self.price_list:
            raise ValueError("Invalid pizza size.")
        self.size = size
        self.toppings = toppings
    
    def calculate_price(self):
        base_price = self.price_list[self.size]
        total_price = base_price + self.topping_price * len(self.toppings)
        return total_price
    
    def __str__(self):
        toppings_str = ', '.join(self.toppings) if self.toppings else 'no toppings'
        return f"{self.size.capitalize()} pizza with {toppings_str}: ${self.calculate_price()}"
    
    @classmethod
    def create_margherita(cls, size):
        return cls(size, ['tomato', 'mozzarella', 'basil'])
    
    @classmethod
    def create_pepperoni(cls, size):    
        return cls(size, ['tomato', 'mozzarella', 'pepperoni'])
    
    @classmethod
    def create_veggie(cls, size):
        return cls(size, ['tomato', 'mozzarella', 'bell peppers', 'onions', 'mushrooms'])
    
    @staticmethod
    def validate_size(size):
        if size not in Pizza.price_list:
            raise ValueError("Invalid pizza size.")
    
class PizzaOrder:
    total_orders = 0
    def __init__(self):
        self.pizzas = []
        PizzaOrder.total_orders += 1
        self.order_id = PizzaOrder.total_orders
    def add_pizza(self, pizza: Pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError("Only Pizza instances can be added.")
        self.pizzas.append(pizza)
    def get_total(self):
        return sum(pizza.calculate_price() for pizza in self.pizzas)
    @classmethod
    def get_total_orders(cls):
        return cls.total_orders
    def __str__(self):
        order_details = '\n'.join(str(pizza) for pizza in self.pizzas)
        total_price = self.get_total()
        return f"Order ID: {self.order_id}\nPizzas:\n{order_details}\nTotal Price: ${total_price}"
    
class OrderManager:
    @staticmethod
    def create_order_from_string(order_str):
        import re

        order = PizzaOrder()

        # Find segments that start with a size keyword (small|medium|large)
        # This lets the caller use separators like ',' or ';' and also
        # supports inputs like "large pepperoni, small margherita, medium veggie".
        pattern = re.compile(r"\b(?:small|medium|large)\b[^;]*", flags=re.IGNORECASE)
        matches = pattern.findall(order_str)

        # Fallback: if regex finds nothing, try splitting on ';'
        if not matches:
            candidates = [s.strip() for s in order_str.split(';') if s.strip()]
        else:
            candidates = [m.strip().rstrip(',') for m in matches]

        for entry in candidates:
            if not entry:
                continue
            parts = entry.split()
            size = parts[0].lower()
            rest = ' '.join(parts[1:]).strip().lower()

            # If rest names a known pizza, use factory methods
            if rest.startswith('margherita'):
                pizza = Pizza.create_margherita(size)
            elif rest.startswith('pepperoni'):
                pizza = Pizza.create_pepperoni(size)
            elif rest.startswith('veggie') or rest.startswith('vegetarian'):
                pizza = Pizza.create_veggie(size)
            else:
                # Treat remaining tokens as explicit toppings; also split by commas
                if rest:
                    raw_toppings = re.split(r"[,\s]+", rest)
                    toppings = [t for t in raw_toppings if t]
                else:
                    toppings = []
                pizza = Pizza(size, toppings)

            order.add_pizza(pizza)

        return order
    
    @staticmethod
    def format_receipt(order: PizzaOrder):
        receipt_lines = [f"Receipt for Order ID: {order.order_id}"]
        for pizza in order.pizzas:
            receipt_lines.append(str(pizza))
        receipt_lines.append(f"Total Amount Due: ${order.get_total()}")
        return '\n'.join(receipt_lines)


# Test your code
if __name__ == "__main__":
    # Test factory methods
    pizza1 = Pizza.create_margherita("large")
    pizza2 = Pizza.create_pepperoni("medium")
    pizza3 = Pizza.create_veggie("small")
    print("Individual Pizzas:")
    for pizza in [pizza1, pizza2, pizza3]:
         print(f" {pizza} - ${pizza.calculate_price()}")
    # Test order
    order1 = PizzaOrder()
    order1.add_pizza(pizza1)
    order1.add_pizza(pizza2)
    print(f"\n{order1}")
    # Test order from string
    print("\nOrder from string:")
    order2 = OrderManager.create_order_from_string("large pepperoni, small margherita, medium veggie")
    print(OrderManager.format_receipt(order2))
    print(f"\nTotal orders created: {PizzaOrder.get_total_orders()}")
    