

def dfs(root, graph, seen):
    if root not in seen:
        seen.add(root)
        for neighbour in graph[root]:
            dfs(neighbour, graph, seen)


if __name__ == "__main__":
    graph = {
                3: [],
                4: [6],
                6: [4, 5, 7, 8],
                8: [6],
                7: [6],
                5: [6],
                1: [2],
                2: [1]
            }
    visited = set()
    count = 0
    for root in graph.keys():
        if root not in visited:
            count += 1
            dfs(root, graph, visited)
    
    print(count) 