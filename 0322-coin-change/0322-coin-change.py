class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #using dynamic programming
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        
        for a in range(amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
        
        return dp[amount] if dp[amount]!= amount + 1 else -1
        
        # brute-force
        # numberofcoins, num = -1,0
        # total = 0
        # num1, num2 = 0, 0
        # for n in coins:
        #     while total <= amount:
        #         temp = max(n+num1, n+num2)
        #         num1 = num2
        #         num2 = temp
        #         total += num1 + num2
        #         numberofcoins += 1
        #     num = numberofcoins
        #     numberofcoins = min(numberofcoins, num )
        # return numberofcoins
                
                
            
        