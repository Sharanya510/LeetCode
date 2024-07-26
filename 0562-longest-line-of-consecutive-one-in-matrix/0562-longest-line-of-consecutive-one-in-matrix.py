class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        
        rows, cols = len(M), len(M[0])
        ones = 0
        # Create a 3D DP array with dimensions (rows x cols x 4)
        dp = [[[0]*4 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if M[i][j] == 1:
                    dp[i][j][0] = dp[i][j-1][0] + 1 if j > 0 else 1  # horizontal
                    dp[i][j][1] = dp[i-1][j][1] + 1 if i > 0 else 1  # vertical
                    dp[i][j][2] = dp[i-1][j-1][2] + 1 if i > 0 and j > 0 else 1  # diagonal
                    dp[i][j][3] = dp[i-1][j+1][3] + 1 if i > 0 and j < cols - 1 else 1  # anti-diagonal
                    
                    ones = max(ones, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        
        return ones