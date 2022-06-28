# create a class
# import math

class Rectangle:
    def __init__(self, length, breadth) -> None:
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)

rect1 = Rectangle(4, 6)
print(rect1.perimeter())
print(rect1.area())
        
        
    