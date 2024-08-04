class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        
        for right in range(len(nums)):
            for left in range(0, right):
                dp[(right, nums[right] - nums[left])] = dp.get((left, nums[right] - nums[left]), 1) + 1   
        
        return max(dp.values())
    
# dp = {}
# right = 0
# left = nothing
# right = 1
# left = 0
# dp[1, 6 - 3] = dp.get[0, 6 - 3] + 1 = 0 + 1 = 1 --> dp[1, 3]

# right = 2
# left = 0
# dp[2, 9 - 3] = dp.get[0, 9 - 3] + 1 = 0 + 1 = 1--> dp[2, 6]
# left = 1
# dp[2, 9 - 6] = dp.get[1, 9 - 6] + 1 = 1 + 1 = 2--> dp[2, 3]

# right= 3
# left = 0
# dp[3, 12 - 3] = dp.get[0, 12 - 3] + 1 = 0 + 1 = 1--> dp[3, 9]
# left = 1
# dp[3, 12 - 6] = dp.get[1, 12 - 6] + 1 = 0 + 1 = 1--> dp[3, 6]
# left = 2
# dp[3, 12 - 9] = dp.get[2, 12 - 9] + 1 = 2 + 1 = 3--> dp[3, 3]