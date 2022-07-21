#!/usr/bin/python3
"""script that defines a square class that defines a square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of the square
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of the square
        Returns: Nothing
        """
        self.__size = size
