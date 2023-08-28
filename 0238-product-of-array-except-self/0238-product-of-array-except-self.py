class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # BRUTE-FORCE
#         nums1 = [1 for i in range(len(nums))]
#         nums2 = [1 for i in range(len(nums))]
        
#         for i in range(len(nums)-1):
#             nums1[i+1] = nums1[i] * nums[i]
#         print(nums1)
        
#         for j in range(len(nums)-1, 0, -1):
#             nums2[len(nums)-j] = nums2[len(nums)-j-1] * nums[j]
#         print(nums2)
        
#         nums3 = [1 for i in range(len(nums))]
        
#         for i in range(len(nums)):
#             nums3[i] = nums1[i] * nums2[len(nums) - 1 - i]
#         return nums3
        
        
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
                
        