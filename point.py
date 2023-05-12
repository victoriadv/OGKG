import sys
import numpy as np


class Point:
    p0 = None

    def __init__(this, x: float, y: float):
        this.__x = x
        this.__y = y

    def __str__(this):
        return f"({this.__x}; {this.__y})"

    def __eq__(this, other) -> bool:
        return this.__x == other.__x and this.__y == other.__y

    def __lt__(this, other) -> bool:
        orientation = Point.p0.orientation(this, other)
        if orientation == 0:
            return Point.p0.distSq(this) < Point.p0.distSq(other)
        return orientation == 2

    def orientation(this, q, r) -> int:
        val = (q.__y - this.__y) * (r.__x - q.__x) - (q.__x - this.__x) * (r.__y - q.__y);
        if val == 0:
            return 0  # collinear
        return 1 if val > 0 else 2  # clock or counterclock wise

    def distSq(this, other):
        return (this.__x - other.__x) * (this.__x - other.__x) + (this.__y - other.__y) * (this.__y - other.__y)

    @property
    def x(this):
        return this.__x

    @property
    def y(this):
        return this.__y


def getSorted(points):
    if len(points) < 3:
        return []

    minPoint = Point(sys.maxsize, sys.maxsize)
    index = 0
    for i, p in enumerate(points):
        if p.y < minPoint.y or p.y == minPoint.y and p.x < minPoint.x:
            minPoint = p
            index = i

    Point.p0 = minPoint
    points[0], points[index] = points[index], points[0]

    return np.array(sorted(points))