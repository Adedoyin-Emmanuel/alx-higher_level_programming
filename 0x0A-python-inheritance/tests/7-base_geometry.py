#!/usr/bin/python3
"""A BaseGeometry class based on previous task
public instance method: area(self)
"""


class BaseGeometry:
    """An empty Base Geometry Class.
    Arguments: self
    Returns: null
    """

    def __init__(self):
        pass

    def area(self):
        """An empty Base Geometry Class.
        Arguments: self
        Returns: null
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator function."""
        self.name = name
        self.value = value
        if (type(value) != int):
            raise TypeError(f"{self.name} must be an integer")
        if (self.value <= 0):
            raise ValueError(f"{self.name} must be greater than 0")
