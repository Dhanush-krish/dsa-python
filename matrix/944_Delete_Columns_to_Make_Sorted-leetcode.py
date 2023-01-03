#   https://leetcode.com/problems/delete-columns-to-make-sorted/

# TC => O(n*m)
# SC => O(1)
# where n and m is the row and column length


from typing import *



class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        COL, ROW = len(strs[0]), len(strs)

        for col in range(COL):
            for row in range(1, ROW):
                if (strs[row-1][col] <= strs[row][col]):
                    continue
                
                count += 1
                break

        return count


if __name__ == "__main__":
    obj = Solution()
    strs = ["a","b"]
    ans = obj.minDeletionSize(strs)
    print(ans)