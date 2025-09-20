
# iterative
def bfs(root, graph):
    queue = [root]
    
    while(queue):
        node = queue.pop(0)
        print(node)
        for neighbour in graph[node]:
            queue.append(neighbour)

### bfs for undirected graph
def bfs(root, graph):
    queue = [root]
    visited = set()            # track visited nodes
    visited.add(root)
    
    while queue:
        node = queue.pop(0)
        print(node)
        
        for neighbour in graph[node]:
            if neighbour not in visited:   # only visit unvisited nodes
                queue.append(neighbour)
                visited.add(neighbour)
            
# we use iterative approach for graph == difficult to implements
    

if __name__ == '__main__':

    graph = {
        "a":["b", "c", "e"],
        "b":["d", "e"],
        "c":["e"],
        "d":[],
        "e":[]
    }
    bfs("a", graph)

