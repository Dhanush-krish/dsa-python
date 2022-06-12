class UnionFind():
    def __init__(self, length) -> None:
        self.root = [root for root in range(length)]
        
    def union(self, v1, v2):
        root_v1 = self.find(v1) 
        root_v2 = self.find(v2)
        if root_v1 != root_v2:
            self.root[root_v2] = root_v1
        self.root[v2] = root_v1
    
    def find(self, vertex):
                
        while(self.root[vertex] != vertex):
            vertex = self.root[vertex]
            
        return vertex
    
    def is_connected(self, v1, v2):
        return self.find(v1) == self.find(v2)





if __name__ == '__main__':
    obj = UnionFind(6)
    obj.union(0,1)
    print(obj.root)
    obj.union(1,2)
    print(obj.root)
    obj.union(3,4)
    print(obj.root)
    ans = obj.is_connected(0,5)
    print(ans)