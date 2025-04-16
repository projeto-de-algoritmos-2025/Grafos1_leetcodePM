from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        indegree = [[0] * n for _ in range(m)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # Passo 1: calcular o grau de entrada (indegree) de cada célula
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
                        indegree[i][j] += 1

        # Passo 2: adicionar todos os nós com grau de entrada 0 à fila
        queue = deque()
        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    queue.append((i, j))

        # Passo 3: realizar BFS por "níveis", cada nível é um aumento no caminho
        length = 0
        while queue:
            length += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        indegree[x][y] -= 1
                        if indegree[x][y] == 0:
                            queue.append((x, y))

        return length
