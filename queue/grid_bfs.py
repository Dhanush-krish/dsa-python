#   https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/


class Solution(object):
    def numIslands(self, grid):
        count = 0
        visited = set()
        ROW,COL = len(grid), len(grid[0])
        
        def direction(row,col):
            result = []
            if (row+1 >=0 and row+1 < ROW and col >= 0 and col < COL and grid[row+1][col] == "1"):
                 result.append((row+1, col))
            if (row-1 >=0 and row-1 < ROW and col >= 0 and col < COL and grid[row-1][col] == "1"):
                 result.append((row-1, col))
            if (row >=0 and row < ROW and col-1 >= 0 and col-1 < COL and grid[row][col-1] == "1"):
                 result.append((row, col-1))
            if (row >=0 and row < ROW and col+1 >= 0 and col+1 < COL and grid[row][col+1] == "1"):
                 result.append((row, col+1))
            
            return result
        
        def bfs(pos, grid, visited):
            queue = [pos]
            while queue:
                for _ in range(len(queue)):
                    node = queue.pop(0)
                    visited.add(node)
                    for neighbour in direction(node[0], node[1]):
                        if neighbour not in visited:
                            queue.append(neighbour)
        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs((row,col), grid, visited)
                    # print(visited)
                    count += 1
        return count
    
if __name__ == "__main__":
    grid = [["1"]]
    
    ans = Solution().numIslands(grid)
    print(ans)