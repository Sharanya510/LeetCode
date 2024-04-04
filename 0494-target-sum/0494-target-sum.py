class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # APPROACH -- BOTTOM UP -- ITERATIVE
        total_sum = sum(nums)
        # If the absolute value of target is greater than the total sum, return 0 since it's impossible to reach the target.
        if abs(target) > total_sum:
            return 0

        # The offset is used to shift negative indices to positive indices in the dp array.
        offset = total_sum
        dp = [[0 for _ in range(2 * total_sum + 1)] for _ in range(len(nums) + 1)]
        dp[0][offset] = 1  # Base case: there's one way to have a total of 0 using 0 numbers.

        for i in range(1, len(nums) + 1):
            for j in range(-total_sum, total_sum + 1):
                # Each cell in the dp table is filled by the sum of ways to achieve the sum without the current number
                # and with the current number subtracted and added.
                if j - nums[i-1] + offset >= 0:
                    dp[i][j + offset] += dp[i-1][j - nums[i-1] + offset]
                if j + nums[i-1] + offset <= 2 * total_sum:
                    dp[i][j + offset] += dp[i-1][j + nums[i-1] + offset]

        return dp[len(nums)][target + offset]
        # APPROACH -- TOP DOWN -- RECURSIVE
#         hash_map = {}
#         def helper(index, total):
#             if index == len(nums):
#                 if total == target:
#                     return 1
#                 else:
#                     return 0
#             if (index, total) in hash_map:
#                 return hash_map[(index, total)]
#             res = helper(index + 1, total - nums[index]) + helper(index+1, total + nums[index]) 
#             hash_map[(index, total)] = res
#             # print(hash_map)
#             return res
        
        
#         return helper(0, 0)
        
        # APPROACH -- BRUTE FORCE
        # def helper(index, total):
        #     if index == len(nums):
        #         if total == target:
        #             return 1
        #         else:
        #             return 0
        #     return helper(index+1, total + nums[index]) + helper(index + 1, total - nums[index])
        # return helper(0, 0)
        
        