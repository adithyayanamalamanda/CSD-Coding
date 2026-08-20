class vertex:

    def __init__(self, v_id):
        self.vertex_name = v_id
        self.adjacency_list = []
        self.degree = 0

    def add_adjacent_vertex(self, vertex):
        self.adjacency_list.append(vertex)


class cycle_detection:

    def __init__(self, v):
        self.vertices = v

    def initialize_degrees(self):
        for vertex in self.vertices:
            vertex.degree = 0

        for vertex in self.vertices:
            for adjacent_vertex in vertex.adjacency_list:
                adjacent_vertex.degree += 1

    def detect_cycle(self):
        queue = []

        # Add vertices with degree 0
        for vertex in self.vertices:
            if vertex.degree == 0:
                queue.append(vertex)

        visited_count = 0

        while queue:
            vertex = queue.pop(0)
            visited_count += 1

            # Reduce degree of adjacent vertices
            for adjacent_vertex in vertex.adjacency_list:
                adjacent_vertex.degree -= 1

                if adjacent_vertex.degree == 0:
                    queue.append(adjacent_vertex)

        # Check whether all vertices were processed
        if len(self.vertices) == visited_count:
            print("No cycle detected in the graph")
        else:
            print("Cycle detected in the graph")


# Create vertices
v1 = vertex(1)
v2 = vertex(2)
v3 = vertex(3)
v4 = vertex(4)
v5 = vertex(5)

# Create directed edges
v1.add_adjacent_vertex(v2)

v2.add_adjacent_vertex(v3)
v2.add_adjacent_vertex(v5)

v3.add_adjacent_vertex(v4)

v5.add_adjacent_vertex(v1)

# Store all vertices
vertices = [v1, v2, v3, v4, v5]

# Cycle detection
cd = cycle_detection(vertices)

cd.initialize_degrees()
cd.detect_cycle()