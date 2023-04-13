#!/usr/bin/python
"""This function appends a string at the end of a text file
And also returns the number of characters added.
"""


def append_write(filename="", text=""):
    """This function takes 2 arguments: filename and text.
    Returns: The number of characters appended to the opened file.
    """
    with open(filename, "a", encoding="utf-8") as file_opened:
        characters_written = file_opened.write(text)
        return (characters_written)
