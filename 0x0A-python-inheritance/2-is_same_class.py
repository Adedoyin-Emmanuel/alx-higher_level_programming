#!/usr/bin/python3
"""A function that returns True if the object is exactly
an instance of the specified class; otherwise False.
"""


def is_same_class(obj, a_class):
    """A function that checks if an object
    is an instance of a specified class.
    Arguments:
        obj: the object to check if is an instance of.
        a_class: the class to check against.
    """
    return isinstance(obj, a_class)
