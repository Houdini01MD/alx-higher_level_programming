#!/usr/bin/python3
"""Area and Perimeter"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Rectangle constructor.


        Args:
            with : the width of rectangle
            height : the height of rectangle
        """
        self.width = width
        self.height = height

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
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calcul rectangle area : width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """calcul rectangle perimeter : 2*(width + height)"""
        return 2 * (self.__width + self.__height)
