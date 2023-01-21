# def dfs (graph,node,destination,visited):
    
#     if visited is None:
#         visited = set()

#     if node == destination:
#         return True
    
#     if node not in visited:
#         visited.add(node)
#         for vertex in graph[node]:
#             if dfs(graph,vertex,destination,visited):
#                 return True
    
#     return False

def dfs(start, destination, graph):

    if start not in graph or destination not in graph:
        return False
    
    stack = [start]
    visited = set()

    while(stack):
        node = stack.pop()
        if node == destination:
            return True
        if node not in visited:
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)

    return False


# graph = dict()
# N = int(input())
# for _ in range(N):
#     graph[int(input())] = []

# E = int(input())
# for _ in range(E):
#     u,v = map(int,input().split())
#     graph[u].append(v)

# root = int(input())
# destination = int(input())
# visited = set()
# print(dfs(graph,root,destination,visited))

start = 7
destination = 9
graph = {
            2: [9], 
            5: [], 
            7: [2,9], 
            9: [5]
        }

print(dfs(start,destination, graph))





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
