# def dfs(node, graph, seen = None):

#     if seen is None:
#         seen = set()

#     stack = [node]
#     seen.add(node)
#     while(stack):
#         node = stack.pop()
#         print(node)

#         for nbr in graph[node]:
#             if nbr not in seen :
#                 stack.append(nbr)
#                 seen.add(nbr)


def dfs(node, graph, seen=None):
    if seen is None:
        seen = set()

    seen.add(node)        
    print(node)

    for nbr in graph[node]:
        if nbr not in seen:
            dfs(nbr, graph, seen)

    return seen



graph = {
    "a":["b", "c", "e"],
    "b":["d", "e"],
    "c":["e"],
    "d":[],
    "e":[]
}


dfs("a", graph)
