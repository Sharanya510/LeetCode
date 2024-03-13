class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(num):
            if num <= 3:
                return num
            
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp(num - i))
            
            return ans

        if n <= 3:
            return n - 1
        
        return dp(n)
    
    
# n = 10
# i = 2
# ans = max(10, 2 * dp(8)) --> 32

# i = 3
# ans = max(10, 3 * dp(7)) --> 36

# i = 4
# ans = max(10, 4 * dp(6)) --> 32

# i = 5
# ans = max(10, 5 * dp(5)) --> 25

# i = 6
# ans = max(10, 6 * dp(4)) --> 24

# i = 7
# ans = max(10, 7 * dp(3)) --> 14

# dp(3) = 2
# dp(2) = 1
# dp(4) = max(4, 2 * 1, 3* 0) = 4
# dp(5)= max(5, 2 * dp(3), 3 * dp(2), 4* dp(1)) = max(5, 4, 1, 0) = 5
# dp(6) = max(6, 2*dp(4), 3*dp(3), 4*dp(2), 5*dp(1)) = max(6, 8, 6, 5) = 8
# dp(7) = max(7, 2*dp(5), 3 * dp(4), 4 * dp(3), 5* dp(2), 6*dp(1)) = max(7, 10, 12, 8, 5, 0) = 12
# dp(8) = max(8, 2*dp(6), 3*dp(5), 4*dp(4), 5*dp(3), 6*dp(2), 7*dp(1)) = max(8, 16, 15, 16, 6, 0) = 16