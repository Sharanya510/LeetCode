class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        row = len(heights)
        col = len(heights[0])
        pacific_queue = deque()
        atlantic_queue = deque()
        
        for i in range(row):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, col - 1))
        for j in range(col):
            pacific_queue.append((0, j))
            atlantic_queue.append((row-1, j))
        
        pacific_bfs = self.bfs(pacific_queue, heights)
        atlantic_bfs = self.bfs(atlantic_queue, heights)
        return list(pacific_bfs.intersection(atlantic_bfs))
    
    
    def bfs(self, queue, heights):
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited=set()
        while queue:
            x, y = queue.popleft()
            visited.add((x, y))
            for dirs in directions:
                new_x = dirs[0] + x
                new_y = dirs[1] + y
                if 0<=new_x< len(heights) and 0<=new_y < len(heights[0]) and (new_x, new_y) not in visited and heights[new_x][new_y] >= heights[x][y]:
                    queue.append((new_x, new_y))
                       
        return visited
        
        
        