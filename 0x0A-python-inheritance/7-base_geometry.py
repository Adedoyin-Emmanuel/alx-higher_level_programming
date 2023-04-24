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

    def integer_validator(self, name, value):
        """Integer validator function."""
        self.name = name
        self.value = value
        if (type(value) != int):
            raise TypeError("{:e} must be an integer".format(self.name))
        if (self.value <= 0):
            raise ValueError(
                "{:e} must be an greater than 0".format(self.name))
