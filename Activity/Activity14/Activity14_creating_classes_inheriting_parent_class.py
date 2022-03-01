# Activity 14: Creating Classes and Inheriting from a Parent Class
# ------------------------------------------------------------------------------



class Polygon:
    """Parent class square and rectangle"""

    def __init__(self, side_len) -> None:
        self.side_len = side_len

    @property
    def num_sides(self):
        return len(self.side_len)

    @property
    def perimeter(self):
        return (sum(self.side_len) * 2)

    def __str__(self) -> str:
        return 'Polygon with %s sides' % (self.num_sides)


class Rectangle(Polygon):
    def __init__(self, height, width) -> None:
        super().__init__([height, width])

    @property
    def area(self):
        return self.side_len[0] * self.side_len[1]


rectangle = Rectangle(10, 15)
print(rectangle.area,
      rectangle.perimeter)


class Square(Rectangle):
    def __init__(self, height, width) -> None:
        super().__init__(height, width)


square = Square(5, 5)
print(square.area,
      square.perimeter)
