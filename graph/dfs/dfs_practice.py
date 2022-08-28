def dfs (graph,node,destination,visited):
    
    if node not in visited:
        visited.add(node)
        if node == destination:
            return 1
        for vertex in graph[node]:
            if dfs(graph,vertex,destination,visited):
                return 1
    
    return 0

graph = dict()
N = int(input())
for _ in range(N):
    graph[int(input())] = []

E = int(input())
for _ in range(E):
    u,v = map(int,input().split())
    graph[u].append(v)

root = int(input())
destination = int(input())
visited = set()
print(dfs(graph,root,destination,visited))

# root = 7
# destination = 9
# graph = {
#             2: [9], 
#             5: [], 
#             7: [2,9], 
#             9: [5]
#         }





"""
4
2
5
7
9
4
2 9
7 2
7 9
9 5
7
9
"""
