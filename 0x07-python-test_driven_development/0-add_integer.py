#!/usr/bin/python3

"""
This function returns True or False if it matches the int or float type.It takes 2 parameters and returns a boolean
"""

# a function that adds 2 integers
def add_integer(a, b=98):
    """
        This function adds 2 integers together
        It takes 2 parameters and returns an integer

        Throws a TypeError if a or b is not an integer or a float
    """
    if((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))