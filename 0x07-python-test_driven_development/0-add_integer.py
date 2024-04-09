#!/usr/bin/python3
"""Module for add_integer"""

def add_integer(a, b=98):
    """function adds 2 integers.
       Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if type(a) not in (int,float):
        raise TypeError('a must be an integer')
    if type(b) not in (int,float):
        raise TypeError('b must be an integer')
    return int(a) + int (b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
