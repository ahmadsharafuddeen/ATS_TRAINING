class Rectangle:
    def __init__(self, x_y_left: tuple, x_y_right: tuple) -> None:
        self.coordinates = (x_y_left, x_y_right)
        self.x_coord = self.coordinates[0][0]
        self.y_coord = self.coordinates[0][1]

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, rect_tuple):
        x_coord1, y_coord1 = rect_tuple[0][0], rect_tuple[0][1]
        x_coord2, y_coord2 = rect_tuple[1][0], rect_tuple[1][1]
        if x_coord1 != x_coord2 or y_coord1 != y_coord2:
            raise ValueError(f'{x_coord1} != {x_coord2} or {y_coord1} != {y_coord2}')
        if x_coord1 > 20 or x_coord2 > 20 or y_coord1 > 20 or y_coord2 > 20:
            raise ValueError('Any coordinate must not be > 20')
        self._coordinates = rect_tuple

    def __str__(self):
        return f"{(self.coordinates)}"

    def area(self):
        return self.x_coord * self.y_coord

    def perimeter(self):
        return 2 * (self.x_coord + self.y_coord)

    def is_square(self):
        return self.x_coord == self.y_coord

    def get_length(self):
        if self.x_coord > self.y_coord:
            return self.x_coord
        else:
            return self.y_coord

    def get_width(self):
        if self.x_coord < self.y_coord:
            return self.x_coord
        else:
            return self.y_coord


rect = Rectangle((8, 8), (8, 8))
print(rect)
print(rect.area())
print(rect.perimeter())
print(rect.get_width())
print(rect.is_square())

