

import grp


def dfs(root, graph, visited):
    if root not in visited:
        visited.add(root)
        count = 1
        for neighbour in graph[root]:
            count += dfs(neighbour, graph, visited)
        return count
    return 0
    
        


if __name__ == "__main__":
    graph = {
                '0': ['8', '1', '5'],
                '1': ['0'],
                '5': ['0', '8'],
                '8': ['0', '5'],
                '2': ['3', '4'],
                '3': ['2', '4'],
                '4': ['3', '2']
                }
    max_cmp = 0
    visited = set()
    
    for root in graph:
        if root not in visited:
            max_cmp = max(max_cmp, dfs(root, graph, visited))
            print(max_cmp)