from graphics import Point, Circle, Line, Text
from flat_geometry import point_in_line_area, points_distance, point_on_line, lines_intersection
import tri_graph

ACCURACY = 10


class GraphPoint:
    def __init__(self, point):
        self.point = point
        self.vertex = tri_graph.TriGraphVertex()


class GraphLine:
    def __init__(self, v1, v2):
        self.v2 = v2
        self.v1 = v1
        self.v_points = [v1, v2]

    def line_parameters(self):
        direction = (self.v2.point.y - self.v1.point.y) / (self.v2.point.x - self.v1.point.x)
        translation = self.v1.point.y - direction * self.v1.point.x
        return direction, translation


def draw_new_point(p, win):
    c = Circle(p, ACCURACY)
    c.setFill('red')
    c.draw(win)


def exit_win(point, win):
    return point.x > win.getWidth() - 100 and point.y > win.getHeight() - 30


def draw(win):
    lines = []
    exit_txt = Text(Point(win.getWidth() - 60, win.getHeight() - 15), 'COMPUTE')
    exit_txt.draw(win)
    while True:
        p1 = win.getMouse()
        if exit_win(p1, win):
            break

        handle_points(p1, lines, win)

    if len(lines) > 0:
        return lines[0].v1.vertex
    else:
        return None


def handle_points(p1, lines, win):
    point_line = find_line_for_point(p1, lines)
    if point_line:
        g1 = new_or_old_point(p1, point_line, win)
    else:
        g1 = GraphPoint(p1)
        draw_new_point(p1, win)

    connect_first_point(g1, lines, win)


def find_line_for_point(point, lines):
    for line in lines:
        if point_in_line_area(line, point):
            px = point_on_line(line, point)
            if points_distance(px, point) < ACCURACY:
                return line

    return None


def new_or_old_point(px, line, win):
    for v_point in line.v_points:
        if points_distance(v_point.point, px) < ACCURACY:
            return v_point

    gx = GraphPoint(px)
    line.v_points.append(gx)
    gx.vertex.add_node_on_line(line.v1.vertex, line.v2.vertex)
    draw_new_point(px, win)
    return gx


def connect_first_point(g1, lines, win):
    p2 = win.getMouse()
    point_line = find_line_for_point(p2, lines)
    if point_line:
        g2 = new_or_old_point(p2, point_line, win)
    else:
        g2 = GraphPoint(p2)
        draw_new_point(p2, win)

    make_new_line(g1, g2, lines, win)


def make_new_line(g1, g2, lines, win):
    new_line = GraphLine(g1, g2)
    lines.append(new_line)
    g1.vertex.connect_node(g2.vertex)
    handle_possible_intersections(new_line, lines, win)
    win_line = Line(g1.point, g2.point)
    win_line.setWidth(3)
    win_line.draw(win)


def handle_possible_intersections(new_line, lines, win):
    for line in lines:
        if line != new_line:
            px = lines_intersection(line, new_line)
            if px:
                gx = new_or_old_point(px, line, win)
                gx.vertex.add_node_on_line(new_line.v1.vertex, new_line.v2.vertex)
