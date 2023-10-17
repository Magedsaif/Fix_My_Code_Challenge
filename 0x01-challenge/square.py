#!/usr/bin/python3
"""Script that defines a square."""""

class square():
    """Square class."""

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialize Square class."""
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if 'width' in kwargs.keys() and self.height != self.width:
                self.height = self.width
            if 'height' in kwargs.keys() and self.width != self.height:
                self.width = self.height

    def area_of_my_square(self):
        """Area of the square."""
        return self.width * self.height

    def PermiterOfMySquare(self):
        """Perimeter of the square."""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Print the square."""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
