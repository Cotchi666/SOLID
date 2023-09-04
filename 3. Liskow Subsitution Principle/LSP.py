class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def set_length(self, length):
        self.length = length
    def set_width(self, width):
        self.width = width
    def area(self):
        return self.length * self.width
    
class Square(Rectangle):
    def set_length(self, length):
        self.length = length
        self.width = length
    def set_width(self, width):
        self.width = width
        self.length= width


def print_area(rectangle):
    rectangle.set_length(10)
    rectangle.set_width(20)
    area = rectangle.area()
    print(area)
    
rectangle=Rectangle(0,0)
square = Square(0,0)

print_area(rectangle)
print_area(square)