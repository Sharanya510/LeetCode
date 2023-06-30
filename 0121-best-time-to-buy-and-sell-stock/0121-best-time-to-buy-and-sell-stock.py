class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_profit = 0
        min_value = float("inf")
        for i in range(len(nums)):
            if nums[i] < min_value :
                min_value = nums[i]
            if nums[i] - min_value > max_profit:
                max_profit = max(max_profit, nums[i] - min_value)
            
                
        return max_profit
            
        