class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        row = len(heights)
        col = len(heights[0])
        pacific_ocean = deque()
        atlantic_ocean = deque()
        for i in range(row):
            pacific_ocean.append((i, 0))
            atlantic_ocean.append((i, col - 1))
        for j in range(col):
            pacific_ocean.append((0, j))
            atlantic_ocean.append((row - 1, j))
        pacific_bfs = self.bfs(pacific_ocean, heights)
        atlantic_bfs = self.bfs(atlantic_ocean, heights)
        return list(pacific_bfs.intersection(atlantic_bfs))
    
    def bfs(self, queue, heights):
        visited = set()
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            x, y = queue.popleft()
            visited.add((x, y))
            for dirs in directions:
                new_x = x + dirs[0]
                new_y = y + dirs[1]
                if new_x >= 0 and new_x < len(heights) and new_y >= 0 and new_y < len(heights[0]) and heights[new_x][new_y] >= heights[x][y] and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y))
        return visited
                
                