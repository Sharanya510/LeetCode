class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        pacific_queue = deque()
        atlantic_queue = deque()
        row = len(heights)
        col = len(heights[0])
        for i in range(row):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, col - 1))
        for j in range(col):
            pacific_queue.append((0, j))
            atlantic_queue.append((row - 1, j))
        pacific_bfs = self.bfs(heights, pacific_queue)
        atlantic_bfs = self.bfs(heights, atlantic_queue)
        return list(pacific_bfs.intersection(atlantic_bfs))
    
    def bfs(self, heights, queue):
        visited = set()
        while queue:
            directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
            x, y = queue.popleft()
            visited.add((x, y))
            for dirs in directions:
                new_x = x + dirs[0]
                new_y = y + dirs[1]
                if new_x >= 0 and new_x < len(heights) and new_y >= 0 and new_y < len(heights[0]) and (new_x, new_y) not in visited and heights[new_x][new_y] >= heights[x][y]:
                    queue.append((new_x, new_y))
        return visited