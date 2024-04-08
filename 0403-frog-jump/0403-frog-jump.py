class Solution:
    def __init__(self):
        self.mark = {}
        self.dp = [[0 for _ in range(2001)] for _ in range(2001)]
    def canCross(self, stones):
        n = len(stones)
        for i in range(n):
            self.mark[stones[i]] = i
        self.dp[0][0] = 1
        for index in range(n):
            for prevJump in range(n + 1):
                if self.dp[index][prevJump]:
                    if stones[index] + prevJump in self.mark:
                        self.dp[self.mark[stones[index] + prevJump]][prevJump] = 1
                    if stones[index] + prevJump + 1 in self.mark:
                        self.dp[self.mark[stones[index] + prevJump + 1]][prevJump + 1] = 1
                    if prevJump - 1 > 0 and stones[index] + prevJump - 1 in self.mark:
                        self.dp[self.mark[stones[index] + prevJump - 1]][prevJump - 1] = 1
        for prevJump in range(n + 1):
            if self.dp[n - 1][prevJump]:
                return True
        return False
