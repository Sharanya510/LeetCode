class Solution:
    def __init__(self):
        self.res = 0

    def numDistinctIslands(self, grid):
        unique_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    self.res = 0
                    self.check(row, col, 1, grid)
                    unique_islands.add(self.res)
        return len(unique_islands)

    def check(self, row, col, count, grid):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] != 1:
            return
        self.res += count
        grid[row][col] = count
        self.check(row + 1, col, count * 10, grid)
        self.check(row, col + 1, count * 20, grid)
        self.check(row - 1, col, count * 30, grid)
        self.check(row, col - 1, count * 40, grid)
