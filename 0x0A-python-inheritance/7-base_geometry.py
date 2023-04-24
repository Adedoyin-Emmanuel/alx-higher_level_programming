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
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        """Integer validator function."""
        self.name = name
        self.value = value
        if (type(value) != int):
            raise TypeError(f"{self.value} must be an integer")
        if (self.value <= 0):
            raise ValueError(f"{self.value} must be greater than 0")
        
        