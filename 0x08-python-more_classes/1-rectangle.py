#!/usr/bin/python3
"""Real definition of a rectangle"""

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        def width(self, value):
            try:
                if type(value) != int:
                    raise TypeError("width must be an integer")
                elif value < 0:
                    raise ValueError("width must be >= 0")
            except TypeError as ex:
                print(ex)
            except ValueError as ex:
                print(ex)

        def height(self, value):
            try:
                if type(value) != int:
                    raise TypeError("width must be an integer")
                elif value < 0:
                    raise ValueError("height must be >= 0")
            except TypeError as ex:
                print(ex)
            except ValueError as ex:
                print(ex)

