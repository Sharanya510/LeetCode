class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # APPROACH -- BOTTOM UP -- ITERATIVE
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0
        offset = total_sum
        dp = [[0 for _ in range(2 * total_sum + 1)] for _ in range(len(nums) + 1)]
        dp[0][offset] = 1
        for i in range(1, len(nums) + 1):
            for j in range(-total_sum, total_sum + 1):
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
        
        