class Vertex:

    def __init__(self, name):
        self.vertex_name = name
        self.adjacent_vertices = []
        self.visited = False

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)


class Graph:

    def breadth_first_search(self, root):
        queue = [root]
        root.visited = True

        while queue:
            vertex = queue.pop(0)
            print(vertex.vertex_name, end=" ")

            for adjacent_vertex in vertex.adjacent_vertices:
                if not adjacent_vertex.visited:
                    adjacent_vertex.visited = True
                    queue.append(adjacent_vertex)


a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
e = Vertex('E')
f = Vertex('F')
g = Vertex('G')
h = Vertex('H')

a.add_adjacent_vertex(b)
a.add_adjacent_vertex(f)
a.add_adjacent_vertex(g)

b.add_adjacent_vertex(a)
b.add_adjacent_vertex(c)
b.add_adjacent_vertex(d)

c.add_adjacent_vertex(b)

d.add_adjacent_vertex(b)
d.add_adjacent_vertex(e)

e.add_adjacent_vertex(d)

f.add_adjacent_vertex(a)

g.add_adjacent_vertex(a)
g.add_adjacent_vertex(h)

h.add_adjacent_vertex(g)

graph = Graph()
graph.breadth_first_search(a)