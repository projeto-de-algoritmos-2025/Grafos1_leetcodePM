from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        target = "123450"
        start = ''.join(str(num) for row in board for num in row)

        neighbors = {
            0: [1,3], 1: [0,2,4], 2: [1,5],
            3: [0,4], 4: [1,3,5], 5: [2,4]
        }

        queue = deque([(start, 0)])
        visited = set([start])

        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps

            zero = state.index('0')
            for nei in neighbors[zero]:
                new_state = list(state)
                new_state[zero], new_state[nei] = new_state[nei], new_state[zero]
                new_str = ''.join(new_state)
                if new_str not in visited:
                    visited.add(new_str)
                    queue.append((new_str, steps + 1))
        
        return -1
