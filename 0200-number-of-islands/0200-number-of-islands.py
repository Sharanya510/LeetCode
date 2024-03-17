class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # APPROACH --> BFS
        # TIME COMPLEXITY --> O(M x N)
        # SPACE COMPLEXITY --> O(min(M, N))
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    queue.append([i,j])
                    self.bfs( queue, grid )
        return count
    
    def bfs(self, queue, grid):
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            x, y = queue.popleft()
            for dirs in directions:
                new_x = x + dirs[0]
                new_y = y + dirs[1]
                if new_x >=0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]) and grid[new_x][new_y] == "1":
                    queue.append([new_x, new_y])
                    grid[new_x][new_y] = "0"