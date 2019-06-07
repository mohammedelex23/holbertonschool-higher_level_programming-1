#!/usr/bin/python3
"""append_file module"""


def append_write(filename="", text=""):
    """
    function that appends a string to a text file (UTF8) and returns
    the number of characters written
    """

    with open(filename, mode='a', encoding="utf-8") as f:
        return(f.write(text))
