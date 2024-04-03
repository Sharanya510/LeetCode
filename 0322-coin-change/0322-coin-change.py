class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # BOTTOM UP APPROACH -- ITERATIVE
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if  i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
            # print(dp)
        res = dp[-1]
        if res == float('inf'):
            return -1
        else:
            return res
        
# dp = [inf, inf, inf, inf,inf, inf, inf, inf,inf, inf, inf, inf]
#         0   1   2     3    4    5   6   7    8    9   10  11
#      [  0,  1,   1,   2,   2,    ]
        
# dp[1], 1+ dp[0] = inf , 1 + 0 = 1
# i = 2, coin = 1 --> dp[2], 1 + dp[1] --> inf , 1+1 --> 2
# i = 2, coin = 2 --> dp[2], 1 + dp[0] --> inf , 1+0 --> 1
# i = 2, coin = 5 --> dp[2], 1 + dp[-3] --> 
#         APPROACH -- MEMOIZATION
#         TOP DOWN -- RECURSIVE APPROACH
#         mem = {}
#         def dp(amt):
#             if amt == 0:
#                 return 0
#             if amt in mem:
#                 return mem[amt]
#             res = float('inf')
#             for coin in coins:
#                 if amt - coin >= 0:
#                     res = min(res, 1 + dp(amt -coin))
#             mem[amt] = res
#             return res
        
#         res = dp(amount)
#         if res == float('inf'):
#             return -1
#         else:
#             return res
        
        
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
        
        
             