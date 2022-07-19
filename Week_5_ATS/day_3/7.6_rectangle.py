from decimal import Decimal


class Rectangle:
    # attributes
    def __init__(self, length=Decimal('1.0'), width=Decimal('1.0')):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if not (Decimal('0.0') <= value <= Decimal('20.0')):
            raise ValueError(f'{value} must be between 0.0 and 20.0')
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (Decimal('0.0') <= value <= Decimal('20.0')):
            raise ValueError(f'{value} must be between 0.0 and 20.0')
        self.__width = value

    def perimeter(self):
        return 2 * (self.__length + self.width)

    def area(self):
        return self.__length * self.__width


rectangle = Rectangle(6, 8)
print(rectangle.area())
