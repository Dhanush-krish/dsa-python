#   https://leetcode.com/problems/reachable-nodes-with-restrictions/


# T.C =>
# S.C =>


from collections import defaultdict, deque
from typing import *


class Solution:
    def reachableNodes(
        self, n: int, edges: List[List[int]], restricted: List[int]
    ) -> int:
        restricted = set(restricted)

        graph = defaultdict(list)

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        queue = deque([0])
        result = 0
        while queue:
            node = queue.pop()
            restricted.add(node)
            result += 1
            for neighbour in graph[node]:
                if neighbour not in restricted:
                    queue.appendleft(neighbour)

        return result


if __name__ == "__main__":
    obj = Solution()
    n = 7
    edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
    restricted = [4, 2, 1]
    ans = obj.reachableNodes(n, edges, restricted)
    print(ans)
