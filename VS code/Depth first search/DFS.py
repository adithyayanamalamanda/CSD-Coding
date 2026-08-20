visited = set()

def depth_first_search(graph, root):
    S = [root]
    visited.add(root)
    while S:
        vertex = S.pop()
        print(vertex, end ='')
        adjacent_vertices = graph.get(vertex)
        for adjacent_vertex in adjacent_vertices:
            if adjacent_vertex not in adjacent_vertices:
                visited.add(adjacent_vertex)
                S.append(adjacent_vertex)
                
graph = {
    'A':['B','F','G'],
    'B':['A','C','D'],
    'C':['B'],
    'D':['B','E'],
    'E':['D'],
    'A':['B','F','G'],
    }