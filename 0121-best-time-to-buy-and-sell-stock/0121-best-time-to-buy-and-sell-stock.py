class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = float("inf")
        for i in range(len(prices)):
            if prices[i] < min_value:
                 min_value = prices[i]
            if prices[i] - min_value > max_profit:
                max_profit = max(max_profit, prices[i] - min_value)
        return max_profit        