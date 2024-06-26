class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        return self.climb_Stairs(0, n, memo)

    def climb_Stairs(self, i: int, n: int, memo: List[int]) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb_Stairs(i + 1, n, memo) + self.climb_Stairs(i + 2, n, memo)
        return memo[i]


# APPROACH -- BOTTOM UP -- ITERATIVE
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1: return 1
#         if n == 2: return 2
#         dp = [0]  * (n + 1)
#         dp[1] = 1
#         dp[2] = 2
#         for i in range(3, n+1):
#             dp[i] = dp[i - 1] + dp[i - 2]
#         return dp[n]
        
        
        
        
#         return self.helper(n)
    
#     def helper(self, n):
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         if n <= 0:
#             return 0
#         return self.helper(n-1)+ self.helper(n-2)
        
        
        
        
        