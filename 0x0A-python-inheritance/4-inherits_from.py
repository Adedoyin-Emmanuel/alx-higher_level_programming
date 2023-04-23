#!/usr/bin/python3
"""A function that returns True if the object is an
instance of a class that inherited (directly or indirectly)
from the specified class.
"""


def inherits_from(obj, a_class):
    """A function that returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    from the specified class.

    Arguments:
        obj: The object to check. , a_class: The class to compare against
    Returns:
        True if the object is an instance that inherited
        (directly or indirectly) from the specified class
        of the class else False.
    """
    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    return False
