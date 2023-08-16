class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        row = len(grid)
        col = len(grid[0])
        if grid[0][0]!=0:
            return -1
        visited = set()
        visited.add((0,0))
        queue.append([0,0,1])
        while queue:
            neighbor = queue.popleft()
            distance = neighbor[2]
            if neighbor[0] == row - 1 and neighbor[1] == col - 1:
                return distance
            directions = [[0,1],[0,-1],[-1,0],[1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
            for dirs in directions:
                new_i = neighbor[0] + dirs[0]
                new_j = neighbor[1] + dirs[1]
                if new_i >= 0 and new_j >= 0 and new_i < row and new_j < col and grid[new_i][new_j]==0 and (new_i,new_j) not in visited:
                    queue.append([new_i,new_j, distance+1])
                    visited.add((new_i, new_j))
        return -1
                
            
                
        
        