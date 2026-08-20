class vertex:

    def __init__(self, name):
        self.vertex_name = name
        self.adjacent_vertices = []
        self.visited = False

    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)

class graph:

    def __init__(self):
        self.ts_stack = []

    def topological_sort(self, root):
        stack = [root]
        root.visited = True
        while stack:
            vertex = stack.pop()

            for adjacent_vertex in vertex.adjacent_vertices:
                if not adjacent_vertex.visited:
                    adjacent_vertex.visited = True
                    stack.append(adjacent_vertex)

            self.ts_stack.append(vertex) # push the processed vertex to the stack

    def linear_ordering(self):
        for vertex in self.ts_stack:
            print(vertex.vertex_name, end = '->')

cal = vertex('calculus')
la = vertex('linear algebra')
fs = vertex('fourier series')
de = vertex('differential equations')
sp = vertex('stochastic processes')

cal.add_adjacent_vertex(la)
cal.add_adjacent_vertex(de)
cal.add_adjacent_vertex(sp)

la.add_adjacent_vertex(fs)

sp.add_adjacent_vertex(de)

graph = graph()
graph.topological_sort(cal)
graph.linear_ordering()
