# create a class
# import math

class Trapezium:
    def __init__(self, a, b, height) -> None:
        self.a = a
        self.b = b
        self.height = height
        
    def area(self):
        return round(((self.a + self.b) / 2) * self.height, 2)
    
    def perimeter(self, c, d):
        return self.a + self.b + c + d


trapez1 = Trapezium(a=5, b=2, height=6)
print(trapez1.area())
print(trapez1.perimeter(c=3, d=2))
        
        
    