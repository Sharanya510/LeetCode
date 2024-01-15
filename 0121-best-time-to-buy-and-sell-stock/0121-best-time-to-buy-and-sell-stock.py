class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, max_profit = 0, 0
        min_value = float("inf")
        for i in range(len(prices)):
            if min_value > prices[i]:
                min_value = prices[i]
            profit = prices[i] - min_value
            max_profit = max(profit, max_profit)
        return max_profit
    
    # 7   1   5   3   6   4
    # min = 7
    # profit = 0
    # max = 0
    #     min = 1
    #     profit = 0
    #     max = 0
    #         min = 1
    #         profit = 4
    #         max = 4
    #             min = 1
    #             profit = 2
    #             max = 4
    #                 min = 1
    #                 profit = 5
    #                 max = 5
    #                     min = 1
    #                     profit = 3
    #                     max = 5
            