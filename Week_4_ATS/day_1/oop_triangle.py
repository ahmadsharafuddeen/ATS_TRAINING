# create a class
# import math

class Triangle:
    # def __init__(self) -> None:
    #     pass 
    
    def area(self, base, height):
        return round(0.5 * base * height, 2)
    
    def perimeter(self, side_a, side_b, side_c):
        return side_a + side_b + side_c

triangle1 = Triangle()
print(f"Perimeter: {triangle1.perimeter(3, 5, 2)}")
print(f'Area: {triangle1.area(4, 6)}')
        
        
    