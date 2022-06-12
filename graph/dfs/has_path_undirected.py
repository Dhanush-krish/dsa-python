from collections import defaultdict


def dfs(source, destination, graph, visited):
    if source == destination: return True
    if source not in visited:
        visited.add(source)
        
        for node in graph[source]:
            if dfs(node, destination, graph, visited):
                return True
    
    return False

if __name__ == "__main__":
    edges = [
        ["i", "j"],
        ["k", "i"],
        ["j", "k"],
        ["m", "k"],
        ["k", "l"],
        ["o", "n"]
    ]
    
    graph = defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    print(graph)
    src = "i"
    dest = "n"
    print(dfs(src, dest, graph, set()))
        