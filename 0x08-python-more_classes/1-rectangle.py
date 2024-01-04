#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """class Rectangle.
        Args:
            with : the width of rectangle
            height : the height of rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """get/set the width of rectangle"""
            return self.width

        @width.setter
        def width(self, value):
            try:
                if type(value) is not int:
                    raise TypeError("width must be an integer")
                elif value < 0:
                    raise ValueError("width must be >= 0")
            except TypeError as ex:
                print(ex)
            except ValueError as ex:
                print(ex)

        @property
        def height(self):
            """get/set the height of rectangle"""
            return self.width

        @width.setter
        def height(self, value):
            try:
                if type(value) is not int:
                    raise TypeError("height must be an integer")
                elif value < 0:
                    raise ValueError("height must be >= 0")
            except TypeError as ex:
                print(ex)
            except ValueError as ex:
                print(ex)
