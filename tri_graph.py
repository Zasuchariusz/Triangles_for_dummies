from graphics import Point
import collections

Triangle = collections.namedtuple('Triangle', 'v1, v2, v3')


class TriGraphVertex:
    def __init__(self):
        self.lines = []

    def triangles(self):
        return self.triangles_rec(set([]))

    def triangles_rec(self, vertices_met):
        num_of_tri = 0
        for second_vertex in self.nodes_not_met(vertices_met):
            for third_vertex in second_vertex.non_collinear_nod_not_met(vertices_met, self):
                if self in third_vertex.nodes_not_met(vertices_met):
                    num_of_tri += 1

        num_of_tri = num_of_tri // 2
        vertices_met.add(self)
        for node in self.nodes_not_met(vertices_met):
                num_of_tri += node.triangles_rec(vertices_met)

        return num_of_tri

    def nodes_not_met(self, nodes_met):
        for line in self.lines:
            for node in line:
                if node not in nodes_met and node != self:
                    yield node

    def non_collinear_nod_not_met(self, nodes_met, start_node):
        for line in self.lines:
            for node in line:
                if node not in nodes_met and node != self and start_node not in line:
                    yield node

    def connect_node(self, node):
        new_line = {node, self}
        self.lines.append(new_line)
        node.lines.append(new_line)

    def add_node_on_line(self, collinear_vertex1, collinear_vertex2):
        for line in collinear_vertex1.lines:
            if collinear_vertex2 in line:
                line.add(self)
                self.lines.append(line)

