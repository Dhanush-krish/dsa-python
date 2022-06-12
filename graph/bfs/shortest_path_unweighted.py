from collections import defaultdict


def bfs(source, destination, graph, visited):
    queue = [(source, 0)]
    
    while queue:
        node, weight = queue.pop(0)
        if node == destination: return weight
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append((neighbour, weight+1))
    
    return -1
                
            
            
if __name__ == "__main__":
    edges = [
  ['m', 'n'],
  ['n', 'o'],
  ['o', 'p'],
  ['p', 'q'],
  ['t', 'o'],
  ['r', 'q'],
  ['r', 's']
]
    graph = defaultdict(list)
    for v1,v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    src = "m"
    dest = "s"
    print(bfs(src, dest, graph, set()))