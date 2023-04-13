#!/usr/bin/python3
"""
A function that reads a text file (UTF-8)
and prints it to the standard input output.
It throws an error if the filename is not defined
"""


def read_file(filename=""):
    """Takes an argument: filename
    Prints the text file content
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
        