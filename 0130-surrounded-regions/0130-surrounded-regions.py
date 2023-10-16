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
        
        # below for loop is to check for "0" in the borders
#         if there is any zero in the border, then add it to visited and queue
        for i in range(row):
            for j in range(col):
                if (i == 0 or i == row -1 or j == 0 or j == col - 1) and board[i][j] == "O" :
                    visited.add((i,j))
                    queue.append([i,j])
            
#      for the values added prior, if there is any connected zero, then you skip
# for the values added prior, if there are no connecting zeros, which means for a value if there is only X then add those to visited and then loop over that
        while queue:
            x, y = queue.popleft()
            directions = [[0,1], [0, -1], [1,0], [-1, 0]]
            for dirs in directions:
                new_x = dirs[0] + x
                new_y = dirs[1] + y
                if new_x >= 0 and new_x < len(board) and new_y >= 0 and new_y < len(board[0]) and  (new_x, new_y) not in visited and board[new_x][new_y] == "O":
                    visited.add((new_x, new_y))
                    queue.append([new_x,new_y])
        
#         values not in visited should be marked as X
        for i in range(row):
            for j in range(col):
                if (i,j) not in visited and board[i][j] == "O":
                    board[i][j] = "X"
        return board
                    
                
        