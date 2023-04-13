#!/usr/bin/python3

""" A function that reads a text file (UTF-8) and prints it to the standard input output. It throws an error if the filename is not defined"""


def read_file(filename=""):
    """Takes an argument: filename
    Prints the text file content
    """
    if(not filename):
        raise ValueError("Filename must be specified")
    with open(filename, 'r', encoding="utf8") as file:
        file_content = file.read()
        print(file_content)