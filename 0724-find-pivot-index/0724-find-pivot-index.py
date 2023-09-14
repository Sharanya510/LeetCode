class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i,n in enumerate(nums):
            if left_sum == (total_sum - left_sum - n):
                return i
            left_sum += n
        return -1
        
#         left, right = 0, len(nums) - 1
#         left_sum, right_sum = nums[left], nums[right]
#         while left < right:
#             if left_sum == right_sum and left+1 != right:
#                 return left + 1
#             elif left_sum < right_sum:
#                 left += 1
#                 left_sum += nums[left]
#             else:
#                 right -= 1
#                 right_sum += nums[right]
#         return -1
                
        
        
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # return -1