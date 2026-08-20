'''
due to the outbreak of the corona virus, every ine of us been qurantined for months without being able to see our frnds or relatives.

there are 2 frnds in our story namely javed and mohan. before the outbreak of the virus, they were very close to each other and used to meet every day. but due to the outbreak of the virus, they have been separated from each other for a long time. 



input:
------
1. T is number of test cases 
2. 
'''

n, x, y = input().split()

graph = {}
i = 1

while i <= n:
    a,b = input().split()
    
    if a not in graph:
        graph[a] = []

    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

    i += 1

queue = [x]
visited = set()
visited.add(x)

flag = False
while queue:
    connect = queue.pop(0)

    if connect == y:
        flag = True
        break

    contacts = graph[connect]
    for contact in contacts:
        if contact not in visited:
            visited.add(contact)
            queue.append(contact)

if flag:
    print("YES")
else:
    print("NO")


