from decimal import Decimal
import math

class Complex:
    # i = math.sqrt(-1)

    def __init__(self, **kwargs):
        self.first_real = Decimal(kwargs.get('first_real', 0))
        self.second_real = Decimal(kwargs.get('second_real', 0))
        self.first_imaginary = Decimal(kwargs.get('first_imaginary', 0))
        self.second_imaginary = Decimal(kwargs.get('first_imaginary', 0))

    def __str__(self):
        return f"({self.first_real}, {self.first_imaginary}i), ({self.second_real}, {self.second_imaginary}i)"

    def add_complex_nums(self):
        return f"{self.first_real + self.second_real} + {self.second_imaginary + self.second_imaginary}i"

    def sub_complex_nums(self):
        return f"{self.first_real - self.second_real} + {self.second_imaginary - self.second_imaginary}i"

complex1 = Complex(first_real=3, second_real=5, first_imaginary=1, second_imaginary=3)
print(complex1)