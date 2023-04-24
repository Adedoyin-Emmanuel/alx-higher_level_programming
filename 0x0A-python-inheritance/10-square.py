#!/usr/bin/python3
"""A Square class that inherits from
the Rectangle class.
"""
RectangleClass = __import__("9-rectangle").Rectangle


class Square(RectangleClass):
    """A square class that inherits from Rectangle class."""

    def __init__(self, size):
        self.self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
