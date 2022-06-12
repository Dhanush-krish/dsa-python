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

from heapq import heapify
from math import dist
import sys
from collections import defaultdict


def bfs(source, destination, graph):
    visited = set()
    dist_path = {key:{"dist":sys.maxsize, "path":[]}for key in graph}
    dist_path[source]["dist"] = 0
    node = source
    
    for _ in range(len(graph)):
        min_node = []
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    cost = dist_path[node]["dist"] + graph[node][neighbour]
                    if (cost < dist_path[neighbour]["dist"]):
                        dist_path[neighbour]["dist"] = cost
                        dist_path[neighbour]["path"] = dist_path[neighbour]["path"] + [node]
                    min_node.append([cost, neighbour])
            heapify(min_node)
            if min_node:
                node = min_node[0][1]
            else:
                return dist_path[destination]
    
    return dist_path[destination]


if __name__ == "__main__":
    graph = defaultdict(dict)
    # n_nodes = int(input())
    # for n_nodes in range(n_nodes):
    #     graph[int(input())] = {}
    
    # print(graph)
    
    # n_edges = int(input())
    # for _ in range(n_edges):
    #     v1, v2, t = map(int, input().split())
    #     graph[v1][v2] = t
    # print(graph)
    # src = int(input())
    # dest = int(input())
    
    graph = {5:{}, 2: {9: 2}, 7: {2: 3, 9: 7}, 9: {5: 1}}
    src = 7
    dest = 9
    destination = bfs(src, dest, graph)
    print(destination["dist"], destination["path"]+[dest])
    