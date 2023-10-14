class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        queue = deque()
        queue.append(start)
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        
        while queue:
            i, j = queue.popleft()
            if i == destination[0] and j == destination[1]:
                print(i, j)
                return True
            visited.add((i, j))
            for dirs in directions:
                old_x, old_y = i, j
                new_x = dirs[0] + i
                new_y = dirs[1] + j
                while new_x>=0 and new_x<len(maze) and new_y>=0 and new_y<len(maze[0]) and maze[new_x][new_y]!=1:
                    old_x = new_x
                    old_y = new_y
                    new_x = new_x + dirs[0]
                    new_y = new_y + dirs[1]
                if (old_x, old_y) not in visited:
                    queue.append((old_x, old_y))
                
        return False