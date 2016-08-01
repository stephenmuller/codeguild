"""Module containing the Rectangle class"""
from point import Point

class Rectangle:
    """A class for representing a rectangle"""

    def __init__(self, point, width, height):
        self.point = point
        self.width = width
        self.height = height

    def __eq__(self, other):
        return (
            self.point == other.point and
            self.width == other.width and
            self.height == other.height
            )

    def __repr__(self):
        return 'Rectangle({!r}, {!r}, {!r})'.format(
            self.point,
            self.width,
            self.height
        )
