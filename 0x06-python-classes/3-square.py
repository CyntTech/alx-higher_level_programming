#!/usr/bin/python3
"""script that defines a class square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of the square
        Returns:
            Nothing
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calculation of the area of square
        Returns:
            Area square
        """
        return (self.__size) ** 2
