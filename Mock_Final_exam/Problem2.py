#Create a Rectangle class with width and height attributes, and methods to calculate area and perimeter.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
# Example usage:
rect = Rectangle(5, 10)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")