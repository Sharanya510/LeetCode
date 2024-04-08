class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        destination = (ROWS-1, COLS-1)
        visited = set()
        queue = []
        queue.append((0, 0, 0))
        visited.add((0, 0))
        heapq.heapify(queue)
        while queue:
            obsc, row, col = heapq.heappop(queue)
            if (row, col) == destination:
                return obsc
            for rd, cd in directions:
                r = rd + row
                c = cd + col
                if r in range(0, ROWS) and c in range(0, COLS) and (r, c) not in visited:
                    newObsc = obsc + grid[r][c]
                    heapq.heappush(queue, (newObsc, r, c))
                    visited.add((r, c))