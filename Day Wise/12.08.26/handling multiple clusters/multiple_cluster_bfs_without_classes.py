graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A'],
    'D': ['A', 'E'],
    'E': ['D'],
    'F': ['G', 'H', 'I'],
    'G': ['F'],
    'H': ['F'],
    'I': ['F']
}

visited = []

def bfs(start):
    queue = [start]
    visited.append(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=' ')

        for adjacent_vertex in graph[vertex]:
            if adjacent_vertex not in visited:
                visited.append(adjacent_vertex)
                queue.append(adjacent_vertex)


for vertex in graph:
    if vertex not in visited:
        bfs(vertex)