class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        prefix = 1
        for i, n in enumerate((nums)):
            res[i] = prefix 
            prefix *= n
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i]
        return res
            
            
            
            
#     1   2   3   4
# 1   1   1   2   6
                        # 1