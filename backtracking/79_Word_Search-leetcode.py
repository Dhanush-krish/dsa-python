#   https://leetcode.com/problems/word-search/


# TC => 
# SC => 


from typing import *



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        seen = set()
    
        def dfs(r, c, l):

            if l == len(word):return True

            if((r < 0) or (r >= ROW)
                or (c < 0) or  (c >= COL)
                or word[l] != board[r][c] 
                or (r,c) in seen):
                return False

            seen.add((r,c))
            res = (dfs(r+1, c, l+1) or
                    dfs(r-1, c, l+1) or
                    dfs(r, c-1, l+1) or 
                    dfs(r, c+1, l+1))
            
            seen.remove((r,c))
            return res


        for r in range(ROW):
            for c in range(COL):
                if dfs(r, c, 0):
                    return True


if __name__ == "__main__":
    obj = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    ans = obj.exist(board, word)
    print(ans)