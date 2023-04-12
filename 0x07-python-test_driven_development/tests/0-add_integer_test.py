#!/usr/bin/python3
import unittest
"""
    Unit tests file for the 0-add_integer.py file
"""

add_integer = __import__("0-add_integer").add_integer


class TestAddInteger(unittest.TestCase):
    """Unit class test for add_integer"""
    def test_module_docString(self):
        # Test for module docstring, at least 10 characters long
        moduleDocstring = __import__("0-add_integer").__doc__
        self.assertTrue(len(moduleDocstring) > 10)
    
    def test_function_docstring(self):
        #Test the function docstring, at least 10 characters long
        functionDocstring = add_integer.__doc__
        self.assertTrue(len(functionDocstring) > 10)
    
    def test_valid_arguments(self):
        # Test the function for valid arguments
        self.assertTrue(add_integer(2,7) == 9)
    
    
    def test_negative_numbers(self):
        # Test the function for string arguments
       self.assertTrue(add_integer(-5, 5) == 0)



if __name__ == "__main__":
    unittest.main()