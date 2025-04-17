from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        if n == 1:
            return 0

        all_visited = (1 << n) - 1
        queue = deque()
        visited = [[False] * (1 << n) for _ in range(n)]

        # Começa de todos os nós com máscara indicando apenas aquele nó visitado
        for i in range(n):
            mask = 1 << i
            queue.append((i, mask, 0))  # (node, visited_mask, steps)
            visited[i][mask] = True

        while queue:
            node, mask, steps = queue.popleft()
            for neighbor in graph[node]:
                next_mask = mask | (1 << neighbor)
                if next_mask == all_visited:
                    return steps + 1
                if not visited[neighbor][next_mask]:
                    visited[neighbor][next_mask] = True
                    queue.append((neighbor, next_mask, steps + 1))
