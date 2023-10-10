class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m=len(grid)
        n=len(grid[0])
        queue=deque()
        fresh=0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append([i,j])
        if fresh == 0:
            return 0
        directions=[[0,1],[-1,0],[1,0],[0,-1]]
        mins=0
        visited=set()
        
        while queue:
            size=len(queue)
            for val in range(size):
                i,j=queue.popleft()
                visited.add((i,j))
                for dirs in directions:
                    new_x=dirs[0]+i
                    new_y=dirs[1]+j
                    if new_x>=0 and new_x<m and new_y>=0 and new_y<n and (new_x, new_y) not in visited and grid[new_x][new_y]!=2 and grid[new_x][new_y]!=0:
                        grid[new_x][new_y]=2
                        queue.append([new_x,new_y])
                        fresh-=1
            mins+=1
            
        if fresh==0:
            return mins-1
        return -1
    
                
                
            
                    
                    
        