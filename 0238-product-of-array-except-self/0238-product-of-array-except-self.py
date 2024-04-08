class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # APPROACH --> BRUTE FORCE
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(N)
        left_prefix = [1]*len(nums)
        right_prefix = [1]*len(nums)
        res = [0]* len(nums)
        for i in range(len(nums)-1):
            left_prefix[i+1] = nums[i] * left_prefix[i]
        # print(left_prefix)
        for i in range(len(nums)-2, -1, -1):
            right_prefix[i] = nums[i+1] * right_prefix[i+1]
        # print(right_prefix)
        for i in range(len(res)):
            res[i] = left_prefix[i] * right_prefix[i]
        return res
        
        # APPROACH --> PREFIX SUM
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(1)
#         res = [0]*len(nums)
#         prefix = 1
#         for i, n in enumerate(nums):
#             res[i] = prefix
#             prefix *= n
#         postfix = 1
#         for i in range(len(nums)-1, -1, -1):
#             res[i]*= postfix
#             postfix *= nums[i]
#         return res
            
        