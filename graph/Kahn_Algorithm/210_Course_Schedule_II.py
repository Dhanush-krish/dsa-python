from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indegree = {c:0 for c in range(numCourses)}

        for crs, preq in prerequisites:
            graph[preq].append(crs)
            indegree[crs] += 1
        
        q = [x for x in indegree if indegree[x] == 0]

        result = []
        while q:
            node = q.pop(0)
            result.append(node)

            for nbr in graph[node]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)

        return result if len(result) == numCourses else []