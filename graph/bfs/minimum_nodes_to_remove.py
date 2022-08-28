from collections import defaultdict

def bfs(source, destination, graph, seen):
    queue = [source]
    result = []
    while(queue):
        node = queue.pop(0)
        if node not in seen:
            seen.add(node)
            for neighbour in graph[node]:
                if neighbour == destination:
                    result.append(node)
                queue.append(neighbour)
    return result

if __name__ == "__main__":
    graph = defaultdict(dict)
    n_nodes = int(input())
    for n_nodes in range(n_nodes):
        graph[int(input())] = {}
    
    n_edges = int(input())
    for _ in range(n_edges):
        v1, v2, t = map(int, input().split())
        graph[v1][v2] = t
    print(graph)
    src = int(input())
    dest = int(input())
    distance = bfs(src, dest, graph, set())
    print(distance)
    
    # graph = {
    #         2: [9], 
    #         5: [], 
    #         7: [3,2,9], 
    #         9: [5],
    #         3:[9]
    #     }
    # src = 7
    # dest = 9
    # distance = bfs(src, dest, graph, set())
    # print(distance)