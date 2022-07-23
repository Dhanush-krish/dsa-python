#   https://leetcode.com/problems/clone-graph/



"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        def dfs(node, seen):
            if node in seen: return seen[node]
            
            copy = Node(node.val)
            seen[node] = copy
            
            for neighbour in node.neighbors:
                copy.neighbors.append(dfs(neighbour,seen))
            
            return copy
        
        return dfs(node, {}) if node else None