from shapes import Shape
from math import pi

class ThreeDimensional(Shape):
    
    def __init__(self, x_axis, y_axis, z_axis) -> None:
        super().__init__(x_axis)
        self.y_axis = y_axis
        self.z_axis = z_axis
        
    def get_z_axis(self):
        """returns y_axis"""
        return self.get_z_axis

    
class Cuboid(ThreeDimensional):
    def __init__(self, length, breadth, height) -> None:
        super().__init__(x_axis=length, y_axis=breadth, z_axis=height)
        self.printHello()
       
    @staticmethod 
    def printHello():
        print('Welcome to Cuboid class') 
        
    def area(self):
        return 2 * (self.x_axis * self.y_axis +  self.y_axis * self.z_axis + self.x_axis * self.z_axis)
    
    def perimeter(self):
        return 4 * (self.x_axis + self.y_axis + self.z_axis)
    
cuboid = Cuboid(3, 4, 5)
print(cuboid.perimeter())
        
    
class Sphere(ThreeDimensional):
    def __init__(self, x_axis, y_axis, z_axis) -> None:
        super().__init__(x_axis, y_axis, z_axis)
        
    def area(self):
        return 4 * pi * pow(self.x_axis, 2)
    
    def volume(self):
        return 4 * pi * pow(self.x_axis, 3)
    
    def perimeter(self):
        return pi * pow(self.x_axis, 2)
    
sphere1 = Sphere(4, 4, 5).volume()
print(sphere1)
