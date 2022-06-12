#   https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3914/


from typing import *
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        output = []
        graph = defaultdict(list)
        
        for (v1, v2),w in zip(equations, values):
            graph[v1].append([v2, w])
            graph[v2].append([v1, 1/w])
        print(graph)
        
        
        def dfs(src, dest, res, seen):
            if src == dest: return res
            
            if src not in seen:
                seen.add(src)
                for neighbour, weight in graph[src]:
                    temp = dfs(neighbour, dest, res*weight, seen)
                    if temp != -1:
                        return temp
            
            return -1

        for v1,v2 in queries:
            if (v1 not in graph or v2 not in graph):
                output.append(-1)
            else:
                output.append(dfs(v1, v2, 1, set()))
        
        return output 
            


if __name__ == '__main__':
    obj = Solution()
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    ans = obj.calcEquation(equations, values, queries)
    print(ans)