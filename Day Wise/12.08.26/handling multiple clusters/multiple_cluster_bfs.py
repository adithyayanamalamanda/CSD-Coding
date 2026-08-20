class vertex:

    def __init__(self, name):
        self.vertex_name = name
        self.adjacent_vertices = []
        self.visited = False

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)

class graph:

    def bfs_helper(self, vertices):
        for vertex in vertices:
            if vertex.visited is False:
                vertex.visited = True
                self.breadth_first_search(vertex)

    def breadth_first_search(self, root):
        queue = [root]
        root.visited = True
        while queue:
            vertex = queue.pop(0)
            print(vertex.vertex_name, end = ' ')
            for adjacent_vertex in vertex.adjacent_vertices:
                if not adjacent_vertex.visited:
                    adjacent_vertex.visited = True
                    queue.append(adjacent_vertex)

# construct all the vertex objects

a = vertex('A')
b = vertex('B')
c = vertex('C')
d = vertex('D')
e = vertex('E')
f = vertex('F')
g = vertex('G')
h = vertex('H')
i = vertex('I')

#add all the adjacent vertices to each vertex

a.add_adjacent_vertex(b)
a.add_adjacent_vertex(c)
a.add_adjacent_vertex(d)

b.add_adjacent_vertex(a)

c.add_adjacent_vertex(a)

d.add_adjacent_vertex(a)
d.add_adjacent_vertex(e)

e.add_adjacent_vertex(d)

f.add_adjacent_vertex(g)
f.add_adjacent_vertex(h)
f.add_adjacent_vertex(i)

g.add_adjacent_vertex(f)

h.add_adjacent_vertex(f)

i.add_adjacent_vertex(f)

x = graph()

vertices = [a, b, c, d, e, f, g, h, i]
x.bfs_helper(vertices)
