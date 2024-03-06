class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if self.helper(board, word, i, j, visited, 0):
                    return True
        return False
    
    def helper(self, board, word, row, col, visited, index):
        if index == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index] or (row, col) in visited:
            return False
        
        visited.add((row, col))
        
        res = (self.helper(board, word, row + 1, col, visited, index+1) or
        self.helper(board, word, row - 1, col, visited, index+1) or
        self.helper(board, word, row, col + 1, visited, index+1) or
        self.helper(board, word, row, col - 1, visited, index+1))
        
        visited.remove((row, col))
        
        return res