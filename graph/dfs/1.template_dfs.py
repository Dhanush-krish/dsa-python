

# iterative
def dfs_itr(root, graph):
    stack = [root]
    
    while(stack):
        node = stack.pop()
        print(node)
        for neighbour in graph[node]:
            stack.append(neighbour)


# recursive
def dfs_rec(root, graph):
    print(root)
    for neighbour in graph[root]:
        dfs_rec(neighbour, graph)


if __name__ == '__main__':

    graph = {
        "a":["b", "c", "e"],
        "b":["d", "e"],
        "c":["e"],
        "d":[],
        "e":[]
    }
    dfs_itr("a", graph)
    print("##########")
    dfs_rec("a", graph)
