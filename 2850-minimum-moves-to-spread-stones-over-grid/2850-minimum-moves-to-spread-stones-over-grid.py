class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        extras, zeroes = defaultdict(int), []
        for row in range(3):
            for col in range(3):
                if grid[row][col] > 1:
                    extras[(row, col)] = grid[row][col]
                if grid[row][col] == 0:
                    zeroes.append((row, col))
        return self.backtrack(0, zeroes, extras)
    
    def backtrack(self, index, zeroes, extras):
        if index == len(zeroes):
            return 0
        dist = inf
        curr_zero_x, curr_zero_y = zeroes[index]
        for key, val in extras.items():
            if val > 1:
                extras[key] -= 1
                dist = min(dist, self.backtrack(index + 1, zeroes, extras) + abs(curr_zero_x - key[0])+ abs(curr_zero_y - key[1]))
                extras[key] += 1
        return dist