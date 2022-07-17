#   https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/




import collections
from typing import *


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        n = len(matrix)
        
        for row in range(n):
            for col in range(n):
                if(matrix[row][col] in rows[row] or matrix[row][col] in cols[col]):
                    return False
                rows[row].add(matrix[row][col])
                cols[col].add(matrix[row][col])
        
        return True


if __name__ == '__main__':
    obj = Solution()
    matrix = [[1]]
    ans = obj.checkValid(matrix)
    print(ans)