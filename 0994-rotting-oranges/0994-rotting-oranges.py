class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        minutes=0
        fresh=0
        queue=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        directions=[[0,1],[0,-1],[-1,0],[1,0]]           
        while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                x=node[0]
                y=node[1]
                for dirs in directions:
                    new_x=x+dirs[0]
                    new_y=y+dirs[1]
                    if new_x>=0 and new_x<len(grid) and new_y>=0 and new_y<len(grid[0]) and grid[new_x][new_y]==1 and grid[new_x][new_y]!=0:
                        grid[new_x][new_y]=2
                        fresh-=1
                        queue.append([new_x,new_y])
            minutes+=1
        if fresh==0:
            return minutes-1
        return -1
                
            
        
        