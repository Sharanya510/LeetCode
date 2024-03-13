class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        area = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]
                    
            curr_row = sorted(matrix[row], reverse = True)
            for i in range(cols):
                area = max(area, curr_row[i] * (i+1))
        return area