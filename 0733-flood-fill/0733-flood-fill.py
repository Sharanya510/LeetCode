class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        image_copy=image
        queue=deque()
        queue.append([(sr,sc),image[sr][sc]])
        visited=set()
        visited.add((sr,sc))
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        
        while queue:
            node=queue.popleft()
            position=node[0]
            x=node[0][0]
            y=node[0][1]
            popped_color=node[1]
            image_copy[x][y]=color
            for dirs in directions:
                new_x=dirs[0]+x
                new_y=dirs[1]+y
                if new_x>=0 and new_x<len(image) and new_y>=0 and new_y<len(image[0]) and (new_x,new_y) not in visited and image[new_x][new_y]==popped_color:
                    queue.append([(new_x,new_y),image[new_x][new_y]])
                    visited.add((new_x,new_y))
        return image_copy
                    
                    
                    
                    

                    
            

            
            
            
        
        
        
        
        