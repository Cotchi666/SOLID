from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

def calculate_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area

shapes = [Rectangle(10, 20), Circle(10)]
print(calculate_area(shapes))
