#   https://leetcode.com/problems/surrounded-regions/




from tkinter import Grid
from typing import *


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW,COLUMN = len(board), len(board[0])
        
        # convert the non surrounded to T
        def dfs(r,c):
            if r<0 or r==ROW or c <0 or c == COLUMN or board[r][c] != "O":
                return 
            
            board[r][c] = "T"
            
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        for r in range(ROW):
            for c in range(COLUMN):
                if  board[r][c] == "O" and (r in [0,ROW-1] or c in [0, COLUMN-1]):
                    dfs(r,c)
        
        #convert all O to X
        for r in range(ROW):
            for c in range(COLUMN):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        # convert all T to O
        for r in range(ROW):
            for c in range(COLUMN):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
        return board


if __name__ == '__main__':
    obj = Solution()
    board = [["X","X","X","X"],
             ["X","O","O","X"],
             ["X","X","O","X"],
             ["X","O","X","X"]]
    ans = obj.solve(board)
    print(board)