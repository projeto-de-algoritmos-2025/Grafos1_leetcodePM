from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # Inicializa a fila com laranjas podres e conta as frescas
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # posição e minuto
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        minutes = 0

        # BFS
        while queue:
            r, c, minute = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, minute + 1))
                    minutes = minute + 1

        return minutes if fresh == 0 else -1
