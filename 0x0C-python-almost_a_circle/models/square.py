#!/usr/bin/python3
"""class Square that inherits from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for the size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if (args):
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)

        else:
            for key, value in kwargs.items():
                if key in ["id", "size", "x", "y"]:
                    setattr(self, key, value)

    def __str__(self):
        """magic method returns strings"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))
