class Solution:
    def islandPerimeter(self, grid):
        row, col = len(grid), len(grid[0])
        seen = set()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return self.dfs((r,c), grid, row, col, seen)
        
    def dfs(self, pos, grid, row, col, seen):

        stack = [pos]
        seen.add(pos)
        result = 0

        while(stack):

            position = stack.pop()
            val, nbrs = self.nbrval(position[0], position[1], row, col, grid)
            result += val

            for nbr in nbrs:
                if nbr not in seen:
                    stack.append(nbr)
                    seen.add(nbr)
        
        return result

    def nbrval(self, r,c, row, col, grid):
        neighbours = []
        val = 0
        all_nbr = [(r + 1, c), 
                   (r - 1, c), 
                   (r, c + 1), 
                   (r, c - 1)]
        
        for r1, c1 in all_nbr:

            if (r1 < 0 or r1 > (row - 1) or c1 < 0 or c1 > (col-1)) or (grid[r1][c1] == 0):
                val += 1
            else:
                neighbours.append((r1, c1))
        
        return val, neighbours




if __name__ == "__main__":
    # grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    grid =[[1,0]]
    obj = Solution()
    print(obj.islandPerimeter(grid))