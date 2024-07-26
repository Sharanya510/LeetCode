class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        ##########################################
        # BRUTE FORCE APPROACH
        ##########################################
        if not M:
            return 0
        
        rows, cols = len(M), len(M[0])
        ones = 0
        
        # Horizontal
        for i in range(rows):
            count = 0
            for j in range(cols):
                if M[i][j] == 1:
                    count += 1
                    ones = max(ones, count)
                else:
                    count = 0
        
        # Vertical
        for i in range(cols):
            count = 0
            for j in range(rows):
                if M[j][i] == 1:
                    count += 1
                    ones = max(ones, count)
                else:
                    count = 0
        
        # Upper diagonal
        for i in range(rows + cols - 1):
            count = 0
            for x in range(max(0, i - cols + 1), min(rows, i + 1)):
                y = i - x
                if y < cols and M[x][y] == 1:
                    count += 1
                    ones = max(ones, count)
                else:
                    count = 0
        
        # Lower diagonal
        for i in range(rows + cols - 1):
            count = 0
            for x in range(max(0, i - rows + 1), min(cols, i + 1)):
                y = i - x
                if y < rows and M[y][x] == 1:
                    count += 1
                    ones = max(ones, count)
                else:
                    count = 0
        
        # Upper anti-diagonal
        for i in range(rows + cols - 1):
            count = 0
            for x in range(max(0, i - cols + 1), min(rows, i + 1)):
                y = cols - 1 - (i - x)
                if y >= 0 and M[x][y] == 1:
                    count += 1
                    ones = max(ones, count)
                else:
                    count = 0
        
        # Lower anti-diagonal
        for i in range(rows + cols - 1):
            count = 0
            for x in range(max(0, i - rows + 1), min(cols, i + 1)):
                y = rows - 1 - (i - x)
                if y >= 0 and M[y][x] == 1:
                    count += 1
                    ones = max(ones, count)
                else:
                    count = 0
        
        return ones