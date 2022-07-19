from abc import ABC

class Shape(ABC):
    def __init__(self, x_axis) -> None:
        self.x_axis = x_axis
        
    def get_x_axis(self):
        return self.x_axis
    
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
shape = Shape(2)
print(shape.get_x_axis())
