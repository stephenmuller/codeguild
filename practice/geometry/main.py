"""main function"""

import math
from point import Point
from rectangle import Rectangle


def build_rectangle():
    """Sets up a rectangle for use later."""

    return Rectangle((Point(0, 0)), 5, 5)


def build_point():
    """Sets a point for use later"""

    return Point(1, -8)


def find_distance_between_points(point_1, point_2):
    """calculates the distance between points

    >>> find_distance_between_points(Point(4, 3), Point(0, 0))
    5.0
    """

    x_difference = (point_2.x - point_1.x)**2
    y_difference = (point_2.y - point_1.y)**2
    output = math.sqrt(x_difference + y_difference)

    return output


def check_if_in_rectangle(point_1, rectangle_1):
    """Check if a point is inside of a rectangle

    >>> check_if_in_rectangle(Point(2, 2), Rectangle(Point(1, 1), 5, 5))
    False
    """

    return(
        point_1.x in range(rectangle_1.point.x, (rectangle_1.point.x + rectangle_1.width + 1))
        and
        point_1.y in range((rectangle_1.point.y - rectangle_1.height), rectangle_1.point.y + 1)
    )


def define_center_point(rectangle_1):
    """find the center of a rectangle

    >>> define_center_point(Rectangle(Point(0, 0), 5, 5))
    Point(2.5, -2.5)
    """

    mid_height = rectangle_1.height/2
    mid_width = rectangle_1.width/2

    return Point(rectangle_1.point.x + mid_width, rectangle_1.point.y - mid_height)


def move_point(point_1):
    """moves point one somewhere else

    >>> move_point(Point(1, 1))
    Point(2, 3)
    """

    distance_to_move_x = 1
    distance_to_move_y = 2

    return Point(point_1.x + distance_to_move_x, point_1.y + distance_to_move_y)


def main():
    """main"""
    rectangle_1 = build_rectangle()
    point_1 = build_point()
    print(check_if_in_rectangle(point_1, rectangle_1))
    print(define_center_point(rectangle_1))
    print(find_distance_between_points(Point(4, 4), Point(0, 0)))
    print(move_point(point_1))


main()
