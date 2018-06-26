import math
from graphics import Point

ACCURACY = 10


def points_distance(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def lines_intersection(line1, line2):
    a1_line, b1_line = line1.line_parameters()
    a2_line, b2_line = line2.line_parameters()
    x_intersect = (b2_line - b1_line) / (a1_line - a2_line)
    y_intersect = a1_line * x_intersect + b1_line
    px = Point(x_intersect, y_intersect)
    if point_in_line_area(line1, px, -1) and point_in_line_area(line2, px, -1):
        return px
    else:
        return None


def point_on_line(line, point):
    a_line, b_line = line.line_parameters()
    a_tangent = 1 / a_line
    b_tangent = a_tangent * point.x + point.y
    x_intersect = (b_tangent - b_line) / (a_line + a_tangent)
    y_intersect = a_line * x_intersect + b_line
    return Point(x_intersect, y_intersect)


def point_in_line_area(line, point, acc=ACCURACY):
    yu = line.v1.point.y
    yd = line.v2.point.y
    if line.v1.point.y < line.v2.point.y:
        yu, yd = yd, yu

    xu = line.v1.point.x
    xd = line.v2.point.x
    if line.v1.point.x < line.v2.point.x:
        xu, xd = xd, xu

    return yd - acc < point.y < yu + acc and xd - acc < point.x < xu + acc