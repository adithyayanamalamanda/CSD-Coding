class vertex:
    
    def __init__(self, name):
        self.person_name = name
        self.friends_list = []
        self.visited = False
        
    def add_friend(self, friend):
        self.friends_list.append(friend)
        
class graph:
    
    def depth_first_search(self, root):
        stack = [root]
        root.visited = True
        while stack:
            vertex = stack.pop()
            print(vertex.person_name, end = '=>')
            for friend in vertex.friends_list:
                if not friend.visited:
                    friend.visited = True
                    stack.append(friend)
    
    def dfs_recursive(self, root):
        print(root.person_name, end = '=>')
        for friend in root.friends_list:
            if not friend.visited:
                friend.visited = True
                self.dfs_recursive(friend)
    
    def breadth_first_search(self, root):
        queue = [root]
        root.visited = True
        while queue:
            vertex = queue.pop(0)
            print(vertex.person_name, end = '=>')
            for friend in vertex.friends_list:
                #if not friend.visited:
                 #   friend.visited = True
                  #  queue.append(friend)
                  if friend.visited:
                      continue
                  else:
                      friend.visited = True
                      queue.append(friend)
                
a = vertex('patrik')
b = vertex('DP')
c = vertex('dhana')
d = vertex('swetcha')
e = vertex('pavani')
f = vertex('fayaz')
g = vertex('manoj')
h = vertex('akanksha')

a.add_friend(b)
a.add_friend(f)
a.add_friend(g)

b.add_friend(a)
b.add_friend(c)
b.add_friend(d)

c.add_friend(b)

d.add_friend(b)
d.add_friend(e)

e.add_friend(d)

f.add_friend(a)

g.add_friend(a)
g.add_friend(h)

h.add_friend(g)

graph = graph()
graph.depth_first_search(a)