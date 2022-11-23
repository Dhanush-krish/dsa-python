#   https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

# TC => 
# SC => 


from typing import *
from collections import defaultdict

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        def dfs(x, y, x_graph, y_graph, seen, nodes):

            seen.add((x,y))

            for x_neighb in x_graph[x]:
                if x_neighb not in seen:
                    nodes.append(x_neighb)
                    dfs(x_neighb[0], x_neighb[1], x_graph, y_graph, seen, nodes)

            for y_neighb in y_graph[y]:
                if y_neighb not in seen:
                    nodes.append(y_neighb)
                    dfs(y_neighb[0], y_neighb[1], x_graph, y_graph, seen, nodes)
            
            return len(nodes)
            
        x_graph = defaultdict(list)
        y_graph = defaultdict(list)
        seen = set()
        result = 0

        for x, y in stones:
            x_graph[x].append((x,y))
            y_graph[y].append((x,y))
        
        for x, y in stones:
            if (x, y) not in seen:
                output = dfs(x, y, x_graph, y_graph, seen, [])
                result += output
        
        return result





if __name__ == "__main__":
    obj = Solution()
    stones = [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]
    ans = obj.removeStones(stones)
    print(ans)