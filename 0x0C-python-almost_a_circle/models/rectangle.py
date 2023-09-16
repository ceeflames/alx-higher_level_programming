#!/usr/bin/python3
"""Class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """
        private instance attributes,
        each with its own public getter and setter
    """

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
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle with # characters"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Assigns arguments to attributes:
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)


    def __str__(self):
        """using Magic method for string representation of the rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))


    def to_dictionary(self):
        """Dictionary representation of the Rectangle"""
        return {
                "id":self.id,
                "width":self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
