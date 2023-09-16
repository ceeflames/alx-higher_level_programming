#!/usr/bin/python3
"""class Square that inherits from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """magic method returns strings"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))
