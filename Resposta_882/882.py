import heapq
from collections import defaultdict

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        graph = defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt))
            graph[v].append((u, cnt))

        distances = [maxMoves + 1] * n
        distances[0] = 0
        min_heap = [(0, 0)]

        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > distances[u]:
                continue
            for v, w in graph[u]:
                if d + w + 1 < distances[v]:
                    distances[v] = d + w + 1
                    heapq.heappush(min_heap, (distances[v], v))

        reachableNodes = sum(1 for d in distances if d <= maxMoves)

        reachableSubnodes = 0
        for u, v, cnt in edges:
            a = 0 if distances[u] > maxMoves else min(maxMoves - distances[u], cnt)
            b = 0 if distances[v] > maxMoves else min(maxMoves - distances[v], cnt)
            reachableSubnodes += min(a + b, cnt)

        return reachableNodes + reachableSubnodes
