"""
This module contains the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """A class that represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This method initializes an instance of Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def check_int(self, str_obj, value):
        """Method that checks if value is an integer"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(str_obj))

    def check_gr_0(self, str_obj, value):
        """Method that checks if value is greater than 0"""
        if value <= 0:
            raise ValueError('{} must be > 0'.format(str_obj))

    def check_gr_eq_0(self, str_obj, value):
        """Method that checks if value is greater than or equal to 0"""
        if value < 0:
            raise ValueError('{} must be >= 0'.format(str_obj))

    def area(self):
        """Method that returns the area of a rectangle"""
        return(self.__width * self.__height)

    def display(self):
        """Method that prints out the rectangle"""
        for y in range(self.__y):
            print()
        for row in range(self.__height):
            for x in range(self.__x):
                print(' ', end='')
            for col in range(self.__width):
                print('#', end='')
            print()

    def to_dictionary(self):
        """Method that returns a dictionary representation of itself"""
        rect_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
        return(rect_dict)

    def __str__(self):
        """Method that returns string represenation of the instance"""
        return("[{}] ({}) {}/{} - {}/{}"
               .format(self.__class__.__name__, self.id, self.x,
                       self.y, self.width, self.height))

    def update(self, *args, **kargs):
        """Method that updates the attributes of the instances"""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kargs.items():
                setattr(self, k, v)

    @property
    """Method for getting width"""
    def width(self):
        return(self.__width)

    @width.setter
    """Method for setting width"""
    def width(self, value):
        self.check_int('width', value)
        self.check_gr_0('width', value)
        self.__width = value

    @property
    """Method for getting height"""
    def height(self):
        return(self.__height)

    @height.setter
    """Method for setting height"""
    def height(self, value):
        self.check_int('height', value)
        self.check_gr_0('height', value)
        self.__height = value

    @property
    """Method for getting x"""
    def x(self):
        return(self.__x)

    @x.setter
    """Method for setting x"""
    def x(self, value):
        self.check_int('x', value)
        self.check_gr_eq_0('x', value)
        self.__x = value

    @property
    """Method for getting y"""
    def y(self):
        return(self.__y)

    @y.setter
    """Method for setting y"""
    def y(self, value):
        self.check_int('y', value)
        self.check_gr_eq_0('y', value)
        self.__y = value
