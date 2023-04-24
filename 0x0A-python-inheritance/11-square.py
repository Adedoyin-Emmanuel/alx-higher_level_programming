#!/usr/bin/python3
"""A Square class that inherits from
Rectangle class.
"""
RectangleClass = __import__("9-rectangle").Rectangle


class Square(RectangleClass):
    """Initializes a square class inherited from
    Rectangle class.
    """

    def __init__(self, size):
        "Initliazing square class"
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return ("[Square] {:w} {:w}".format(self.__size, self.__size))
