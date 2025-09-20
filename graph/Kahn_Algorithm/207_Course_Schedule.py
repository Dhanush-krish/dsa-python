from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        indegree = {node:0 for node in range(numCourses)}

        for dest, src in prerequisites:
            graph[src].append(dest)
            indegree[dest] += 1
        
        q = [n for n in indegree if indegree[n] == 0]

        finished = 0

        while q:
            node = q.pop(0)
            finished += 1

            for nbr in graph[node]:
                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    q.append(nbr)
        
        return finished ==  numCourses


        