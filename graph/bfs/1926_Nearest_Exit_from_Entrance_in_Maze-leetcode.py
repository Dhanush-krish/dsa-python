#   https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

# TC => 
# SC => 


from typing import *


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        def bfs(maze, pos):
            ROW, COL = len(maze), len(maze[0])
            start_r, start_c = pos
            maze[start_r][start_c] = "+"
            queue = [(start_r, start_c, 0)]

            while(queue):
                r, c, dist = queue.pop(0)
                for row, col in [[r - 1 , c], [r + 1, c], [r, c + 1], [r, c - 1]]:
                    if 0 <= row < ROW and 0 <= col < COL and maze[row][col] == ".":
                        if(row == 0 or col == 0 or row == (ROW - 1) or col == (COL - 1)):
                            return dist + 1
                        queue.append((row, col, dist + 1))
                        maze[row][col] = "+"
            
            return -1
        
        return bfs(maze, entrance)






if __name__ == "__main__":
    obj = Solution()
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]

    entrance = [1,2]
    ans = obj.nearestExit(maze, entrance)
    print(ans)