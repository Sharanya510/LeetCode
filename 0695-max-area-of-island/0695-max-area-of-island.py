class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        queue = deque()
        row = len(grid)
        col = len(grid[0])
        self.max_area = 0
        self.visited = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area = 1
                    queue.append([i,j])
                    self.bfs(i, j, queue, grid, area)
        return self.max_area
        
    
    def bfs(self, i, j, queue, grid, area):
        directions = [[1,0], [-1, 0], [0,1], [0,-1]]
        while queue:
            i, j = queue.popleft()
            self.visited.add((i,j))
            for dirs in directions:
                new_x = dirs[0] + i
                new_y = dirs[1] + j
                if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0]) and grid[new_x][new_y] == 1 and (new_x, new_y) not in self.visited:
                    grid[new_x][new_y] = 0
                    area += 1
                    queue.append([new_x, new_y])
            
        self.max_area = max(self.max_area, area)