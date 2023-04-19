#!/usr/bin/python3
"""A function that inserts a line of text to a file,
after each line containing specific string.
"""


def append_after(filename=""):
    with open(filename, "r+", encoding="utf-8") as file_opened:
        read_file = file_opened.read()
        while read_file:
            if(not read_file):
                break
            #get the characters
            print(read_file)
            
append_after("tests/0-read_file.txt")
