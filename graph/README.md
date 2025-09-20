## graph
*   graph = node + edges
*   dfs
    * uses stack
    * easy to implement
    * TS = O(N + E) where N is the number of nodes and E is the number of edges
    * SC = O(N)
*   bfs
    * uses queue 
    * no recursive approach
    * used in shortest path algorithm
    * TS = O(N + E) where N is the number of nodes and E is the number of edges
    * SC = O(N)
*   union find
    * finds components (nodes) are connected
*   directed graph => cache is not required
*   undirected graph => cache is required to avoid infinite loop

Order 
- DFS
- BFS
- UnionFind
- Single Source Shortest path (Dijkstra's Algorithm (non negative weights), Bellman Ford Algorithm (including negative weights))
- Kahn's Algorithm
- Spanning Tree (Kruskal's Algorithm, Prim's Algorithm)


### reference
*   https://youtu.be/tWVWeAqZ0WU
*   https://youtu.be/NcGxuF-6Gfg
*   https://leetcode.com/explore/learn/card/graph/
*   https://leetcode.com/discuss/general-discussion/655708/Graph-For-Beginners-Problems-or-Pattern-or-Sample-Solutions
