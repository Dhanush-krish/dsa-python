#   https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3845/


from typing import *


class Solution:
    
    def find(self, v1):
        return self.root[v1]
    
    def union(self, v1, v2):
        root_v1 = self.find(v1)
        root_v2 = self.find(v2)
        
        if root_v1 != root_v2:
            for index in range(len(self.root)):
                if(self.root[index] == root_v2):
                    self.root[index] = root_v1
                    
            
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row = len(isConnected)
        column = len(isConnected)
        self.root = [root for root in range(row)]
        
        for row_i in range(row):
            for column_i in range(column):
                if row_i >= column_i:
                    continue
                elif isConnected[row_i][column_i] == 1:
                    self.union(row_i, column_i)
        
        count = 0
        for index in range(row):
            if self.root[index] == index:
                count += 1
        return count


if __name__ == '__main__':
    obj = Solution()
    matrix = [[1,0,0],[0,1,0],[0,0,1]]
    ans = obj.findCircleNum(matrix)
    print(ans)