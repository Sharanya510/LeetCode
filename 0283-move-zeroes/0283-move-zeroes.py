class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            
         
        
        
# 0   1   0   3   12
# i
# j
#     j
# 1   0   0   3    12
#     j
#     i
#         j
#             j
# 1   3   0   0    12
#         i         j
# 1   3   12  0     0

        
        
#         count = 0
#         for n in nums:
#             if n == 0:
#                 count += 1
#         # print(count)
        
#         i = 0
#         while i < len(nums):
#             if nums[i] == 0:
#                 del nums[i]
#             else:
#                 i += 1
#         # print(nums)
        
#         i = 0
#         while i < count:
#             nums.append(0)
#             i += 1
#         return nums
        