#!/usr/bin/python3
"""Real definition of a rectangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Rectangle constructor.


        Args:
            with : the width of rectangle
            height : the height of rectangle
        """
        self.__width = width
        self.__height = height

        @property
        def width(self):
            """get/set the width of rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """get/set the height of rectangle"""
            return self.__width

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
