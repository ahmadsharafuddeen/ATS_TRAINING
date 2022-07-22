from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, x_axis) -> None:
        self.x_axis = x_axis
        
    def get_x_axis(self):
        return self.x_axis
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
# shape = Shape(2)
# print(shape.get_x_axis())
