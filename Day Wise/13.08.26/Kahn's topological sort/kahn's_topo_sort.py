class vertex:

    def __init__(self, name):
        self.vertex_name = name
        self.adjacency_list = []
        self.degree = 0

    def add_adjacent_vertex(self, vertex):
        self.adjacency_list.append(vertex)


class kahns:

    def __init__(self, v):
        self.vertices = v

    def initialise_degree(self):
        for vertex in self.vertices:
            for adjacent_vertex in vertex.adjacency_list:
                adjacent_vertex.degree += 1

    def kahns_topological_sort(self):

        queue = []

        # Add vertices with in-degree 0
        for vertex in self.vertices:
            if vertex.degree == 0:
                queue.append(vertex)

        topological_order = []

        while queue:

            vertex = queue.pop(0)
            topological_order.append(vertex.vertex_name)

            # Remove the vertex's outgoing edges
            for adjacent_vertex in vertex.adjacency_list:
                adjacent_vertex.degree -= 1

                # If in-degree becomes 0, add to queue
                if adjacent_vertex.degree == 0:
                    queue.append(adjacent_vertex)

        # Check for cycle
        if len(topological_order) != len(self.vertices):
            print("Graph contains a cycle")
        else:
            print("Topological Order:")
            print(" -> ".join(topological_order))


cal = vertex('calculus')
la = vertex('linear algebra')
fs = vertex('fourier series')
de = vertex('differential equations')
sp = vertex('stochastic processes')

cal.add_adjacent_vertex(la)
cal.add_adjacent_vertex(de)
cal.add_adjacent_vertex(sp)

la.add_adjacent_vertex(fs)

de.add_adjacent_vertex(sp)

vertices = [cal, la, fs, de, sp]

kahns_algorithm = kahns(vertices)

kahns_algorithm.initialise_degree()
kahns_algorithm.kahns_topological_sort()