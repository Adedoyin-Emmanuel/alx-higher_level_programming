#!/usr/bin/python3
"""A class that inherits from BaseGeometry class."""


class BaseGeometry:
    """An empty Base Geometry Class.
    Arguments: self
    Returns: null
    """

    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator function."""
        self.name = name
        self.value = value
        if (type(value) != int):
            raise TypeError(f"{self.name} must be an integer")
        if (self.value <= 0):
            raise ValueError(f"{self.name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry class."""

    def __init__(self, width, height):
        """Init a new Rectangle object
        Arguments:
            (width): integer, the width of the rectangle
            (height): integer, the height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns the string representation of the
        rectangle description: [Rectangle] <width>/<height>
        """
        return (f"[Rectangle] {self.__width } / {self.__height}")
