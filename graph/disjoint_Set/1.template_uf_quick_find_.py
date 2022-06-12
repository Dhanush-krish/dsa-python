"""
    Implementation with Quick Find: in this case, the time complexity of the find function will be O(1). 
    However, the union function will take more time with the time complexity of O(N).
"""


class unionFind():
    def __init__(self, length) -> None:
        self.root = [root for root in range(length)]
    
    def find(self, index):
        return self.root[index]
    
    def union(self, v1, v2):
        root_v1 = self.find(v1)
        root_v2 = self.find(v2)
        
        if root_v1 != root_v2:
            for index in range(len(self.root)):
                if self.root[index] == root_v2:
                    self.root[index] = root_v1
                    
    def is_connected(self, v1, v2):
        return self.root[v1] == self.root[v2]
                
        
if __name__ == '__main__':
    obj = unionFind(5)
    obj.union(0, 1)
    obj.union(3, 4)
    ans = obj.is_connected(0,1)
    print(ans)