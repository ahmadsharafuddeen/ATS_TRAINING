from shapes import Shape
from math import pi

class TwoDimensional(Shape):
    
    def __init__(self, x_axis, y_axis) -> None:
        super().__init__(x_axis)
        self.y_axis = y_axis
        
    def get_y_axis(self):
        """returns y_axis"""
        return self.get_y_axis
    
class Triangle(TwoDimensional):
    def __init__(self, x_axis, y_axis, hypotenuse) -> None:
        super().__init__(x_axis, y_axis)
        self.hypotenuse = hypotenuse
        
    def area(self):
        return 0.5 * self.x_axis * self.y_axis
    
    def perimeter(self):
        return self.x_axis + self.y_axis + self.hypotenuse
    
triangle = Triangle(3, 9, 10)
print(triangle.perimeter())
        
    
class Square(TwoDimensional):
    def __init__(self, x_axis, y_axis) -> None:
        super().__init__(x_axis, y_axis)
        assert self.x_axis == self.y_axis
        
    def area(self):
        return pow(self.x_axis, 2)
    
    def perimeter(self):
        return 4 * self.x_axis
    
square1 = Square(4, 4).perimeter()
print(square1)

class Circle(TwoDimensional):
    def __init__(self, x_axis, y_axis) -> None:
        super().__init__(x_axis, y_axis)
        
    def area(self):
        return pi * pow(self.x_axis, 2)
    
    def perimeter(self):
        return 2 * pi * self.x_axis
    
circle1 = Circle(3, 4).area()
print(circle1)

