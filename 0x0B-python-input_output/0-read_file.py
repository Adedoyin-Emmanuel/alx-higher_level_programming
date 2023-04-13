""" A function that reads a text file (UTF-8) and prints it to the standard input output"""


def read_file(filename=""):
    """Takes a argument: filename
    Returns: the text file content
    """
    #throws an error if the filename is not specified
    if(not filename):
        raise ValueError("Filename must be specified")
    with open(filename, encoding="UTF-8") as file:
        read_file = file.read()
        print(read_file)



