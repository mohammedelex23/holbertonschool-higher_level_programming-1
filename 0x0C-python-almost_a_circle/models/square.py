"""
This module contains the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """This method initializes an instance of Square"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Method that returns string represenation of the instance"""
        return("[{}] ({}) {}/{} - {}"
               .format(self.__class__.__name__, self.id, self.x,
                       self.y, self.width)
               )

    @property
    def size(self):
        return(self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
