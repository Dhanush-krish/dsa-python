## prepare graph from input
# graph = {
#     0:{"name":"abc","neighbour":[1,3]},1:{"name":"def","neighbour":[2]},
#     2:{"name":"ghi","neighbour":[4]},3:{"name":"jkl","neighbour":[]},
#     4:{"name":"mno","neighbour":[]}
#     }

# def dfs(root, destination, graph, path):
    
#     if graph[root]["name"] == destination:
#         print(path+graph[root]["name"])
        
#     for neighbour in graph[root]["neighbour"]:
#         dfs(neighbour, destination, graph, path+graph[root]["name"]+"/")

# ## from input
# root = 0
# destination = "ghi"
# dfs(root, destination, graph, "/")

tree = {
    0:{"name":"abc","neighbour":[1,3]},1:{"name":"def","neighbour":[2]},
    2:{"name":"ghi","neighbour":[4]},3:{"name":"jkl","neighbour":[]},
    4:{"name":"mno","neighbour":[]}
    }



def dfs(root,destination, tree):
    stack = [(root, "/")]
    
    while(stack):
        
        _id, parent = stack.pop()
        
        if(tree[_id]["name"] == destination):
            return parent+tree[_id]["name"]
        
        for neighbour in tree[_id]["neighbour"]:
            stack.append((neighbour, parent+tree[_id]["name"]+"/"))
            
print(dfs(0, "mno", tree))