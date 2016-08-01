"""Module containing Point class"""


class Point:
    """A class for representing the points of a rectangle"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (
            self.x == other.x and
            self.y == other.y
        )

    def __repr__(self):
        return 'Point({!r}, {!r})'.format(
            self.x,
            self.y
        )
