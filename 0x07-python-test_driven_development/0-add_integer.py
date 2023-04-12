#!/usr/bin/python3

"""This function returns True or False if it matches the int or float type.It takes 2 parameters and returns a boolean"""


def add_integer(a, b=98):
    """Returns the addition of a and b
    Floating point arguments are typecasred into integers
    Raises:
        TypeError: if a or b is not an integer or a float
    """
    if((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))