
# iterative
def bfs(root, graph):
    queue = [root]
    
    while(queue):
        node = queue.pop(0)
        print(node)
        for neighbour in graph[node]:
            queue.append(neighbour)
            
# we use iterative approach for graph
    

if __name__ == '__main__':

    graph = {
        "a":["b", "c", "e"],
        "b":["d", "e"],
        "c":["e"],
        "d":[],
        "e":[]
    }
    bfs("a", graph)

