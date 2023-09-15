#!/usr/bin/python3
"""Class Rectangle that inherits from Base"""


from models.base import Base

class Rectangle(Base):
    """private instance attributes, each with its own public getter and setter"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """Getter for the width attribute"""
            return self.__width
        @width.setter
        def width(self, value):
            """Setter for the width attribute"""
            if not isinstance(value, int):
                raise ValueError("Width must be an integer.")
            if value < 1:
                raise ValueError("Width must be greater than or equal to 1.")
            self.__width = value

        @property
        def height(self):
            """getter for the height attribute"""
            return self.__height

        @height.setter
        def height(self, value):
            """Setter for the height attribute.

            Args:
                value (int): The new height of the rectangle
            raises:
                ValueError: if value is not an integer or is less than 1
            """
            if not isinstance(value, int):
                raise ValueError("Height must be an integer.")
            if value < 1:
                raise ValueError("Height must be greater than or equal to 1.")
            self.__height = value

        @property
        def x(self):
            """Getter for the x attribute"""
            return self.__x

        @x.setter
        def x(self, value):
            """Setter for the x attribute"""
            if not isinstance(value, int):
                raise ValueError("X must be an integer.")
            if value < 0:
                raise ValueError("X must be greater than or equal to 0.")
            self.__x = value

        @property
        def y(self):
            """Getter for the y attribute"""
            return self.__y

        @y.setter
        def y(self, value):
            """Setter for the y attribute"""
            if not isinstance(value, int):
                raise valueerror("Y must be an integer.")
            if value < 0:
                raise ValueError("Y must be greater than or equal to 0.")
            self.__y = value
