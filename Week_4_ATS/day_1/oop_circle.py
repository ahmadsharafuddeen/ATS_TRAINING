# create a circle class
from cmath import pi

class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
        
    def perimeter(self) -> float: 
        return round(2 * pi * self.radius, 2)
    
    def area(self) -> float:
        return round(pi * pow(self.radius, 2), 2)
    
circle1 = Circle(5) 
print(circle1.perimeter())
print(circle1.area())
        
        
    