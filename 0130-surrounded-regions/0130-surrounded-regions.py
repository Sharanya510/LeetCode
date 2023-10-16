class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        queue = deque()
        row = len(board)
        col = len(board[0])
        visited = set()
        
        for i in range(row):
            for j in range(col):
                if (i == 0 or i == row -1 or j == 0 or j == col - 1) and board[i][j] == "O" :
                    visited.add((i,j))
                    queue.append([i,j])
            
        while queue:
            x, y = queue.popleft()
            directions = [[0,1], [0, -1], [1,0], [-1, 0]]
            for dirs in directions:
                new_x = dirs[0] + x
                new_y = dirs[1] + y
                if new_x >= 0 and new_x < len(board) and new_y >= 0 and new_y < len(board[0]) and  (new_x, new_y) not in visited and board[x][y] == "O":
                    visited.add((new_x, new_y))
                    queue.append([new_x,new_y])
        
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and board[i][j] == "O":
                    board[i][j] = "X"
        return board
                    
                
        