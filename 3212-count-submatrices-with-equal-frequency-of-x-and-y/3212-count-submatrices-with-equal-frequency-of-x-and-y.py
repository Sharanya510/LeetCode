class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        X, Y = [0] * cols, [0] * cols
        res = 0
        for r in range(rows):
            count_X, count_Y = 0, 0
            for c in range(cols):
                count_X += (grid[r][c] == 'X')
                count_Y += (grid[r][c] == 'Y')
                X[c] += count_X
                Y[c] += count_Y
                res += (X[c] > 0) and (X[c] == Y[c])
        return res