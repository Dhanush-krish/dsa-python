

def dfs(source, destination, graph):
    if source == destination: return True
    
    for neighbour in graph[source]:
        if dfs(neighbour, destination, graph):
            return True
    
    return False
    



if __name__ == "__main__":
    graph = {
        "f": ["g", "i"], 
        "g": ["h"], 
        "h": [], 
        "i": ["g", "k"], 
        "j": ["i"], 
        "k": []
        }
    src = "h"
    dest = "f"
    print(dfs(src, dest, graph))
