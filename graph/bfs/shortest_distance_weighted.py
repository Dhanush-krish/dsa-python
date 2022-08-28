"""
4 => number of nodes
2
5
7
9
4 => number of edges
2 9 2
7 2 3
7 9 7 
9 5 1
7 => source
9 => destination
"""

import sys
from collections import defaultdict


def bfs(source, destination, graph):
    distance = {key:sys.maxsize for key in graph}
    distance[source] = 0
    queue = [(0,source)]
    
    while(queue):
        temp = queue.pop(0)
        u = temp[1]
        
        for neighbour in graph[u]:
            if(distance[neighbour] > distance[u]+graph[u][neighbour]):
                if distance[neighbour]!= sys.maxsize:
                    queue.remove((distance[neighbour],neighbour))
                distance[neighbour] = distance[u]+graph[u][neighbour]
                queue.append((distance[neighbour],neighbour))
        
    return -1 if distance[destination] == sys.maxsize else distance[destination]

if __name__ == "__main__":
    graph = defaultdict(dict)
    n_nodes = int(input())
    for n_nodes in range(n_nodes):
        graph[int(input())] = {}
    
    print(graph)
    
    n_edges = int(input())
    for _ in range(n_edges):
        v1, v2, t = map(int, input().split())
        graph[v1][v2] = t
    print(graph)
    src = int(input())
    dest = int(input())
    distance = bfs(src, dest, graph)
    print(distance)
    
    # graph = {5:{7:1}, 2: {9: 2, 3:1}, 7: {2: 3, 9: 7}, 9: {5: 1},3:{}}
    # src = 7
    # dest = 9
    # distance = bfs(src, dest, graph)
    # print(distance)
    
    