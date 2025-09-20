import heapq
from collections import defaultdict

def dijkstra(n, edges, src, undirected=False):
    """
    n: number of nodes (0 to n-1)
    edges: list of tuples (u, v, w)
    src: source node
    undirected: True if edges are undirected
    Returns:
        dist: shortest distances from src to all nodes
        prev: previous node array to reconstruct paths
    """
    
    # 1️⃣ Build adjacency list
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        if undirected:
            graph[v].append((u, w))

    # 2️⃣ Initialize distance array and previous node array
    dist = [float('inf')] * n
    dist[src] = 0
    prev = [None] * n

    # 3️⃣ Min-heap: (distance, node)
    heap = [(0, src)]

    while heap:
        d, node = heapq.heappop(heap)

        # Skip outdated heap entries
        if d > dist[node]:
            continue

        # 4️⃣ Relax edges
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                prev[neighbor] = node
                heapq.heappush(heap, (dist[neighbor], neighbor))

    return dist, prev

# 5️⃣ Function to reconstruct path
def reconstruct_path(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return path[::-1]  # reverse to get path from source to target


edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5)
]
n = 4
src = 0
dist, prev = dijkstra(n, edges, src)

print("Shortest distances:", dist)
print("Shortest path from 0 to 3:", reconstruct_path(prev, 3))
