class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        mem = {}
        def dp(amt):
            if amt == 0:
                return 0
            if amt in mem:
                return mem[amt]
            res = float('inf')
            for coin in coins:
                if amt - coin >= 0:
                    res = min(res, 1 + dp(amt -coin))
            mem[amt] = res
            return res
        
        res = dp(amount)
        if res == float('inf'):
            return -1
        else:
            return res
        
        
#         BRUTE FORCE -- LINE 5 TO 19
#         def dp(amt):
#             if amt == 0:
#                 return 0
            
#             res = float('inf')
#             for coin in coins:
#                 if amt - coin >= 0:
#                     res = min(res, 1 + dp(amt -coin))
            
#             return res
#         res = dp(amount)
#         if res == float('inf'):
#             return -1
#         else:
#             return res
        
        
        
#         dp = [float('inf')]*(amount+1)
#         dp[0] = 0
#         for amt in range(1, amount+1):
#             for coin in coins:
#                 if  amt - coin >= 0:
#                     dp[i] = min(dp[i], 1 + dp[amt-coin])
#         return dp[-1]
        
        
             