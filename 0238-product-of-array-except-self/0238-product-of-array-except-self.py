class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        res = [0]*len(nums)
        
        for i in range(len(nums)):
            res[i] = product
            product *= nums[i]
        # print(res)
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= product
            product *= nums[i]
        # print(res)
        
        return res

        
        
        
        
# p   1   2   3   4
# 1   1   1   2   6
#                     p = 24
#     24  12  8    6
                
        