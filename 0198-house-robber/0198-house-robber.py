class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
        for i in range(N - 2, -1, -1):
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
            
        return maxRobbedAmount[0]    
    
    
    #APPROACH -- TOP DOWN
#     def __init__(self):
#         self.memo = {}
    
#     def rob(self, nums: List[int]) -> int:
#         self.memo = {}
#         return self.robFrom(0, nums)
    
#     def robFrom(self, i, nums):
#         if i >= len(nums):
#             return 0
#         if i in self.memo:
#             return self.memo[i]
#         ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
#         self.memo[i] = ans
#         return ans