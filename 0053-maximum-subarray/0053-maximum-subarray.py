class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum += nums[i]
            if nums[i] > curr_sum:
                curr_sum = nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum
    
    # to print the subarray itself
#     start_idx = 0
#     end_idx = 0
#     curr_sum = nums[0]
#     max_sum = nums[0]
    
#     for i in range(1, len(nums)):
#         if nums[i] > curr_sum + nums[i]:
#             curr_sum = nums[i]
#             start_idx = i
#         else:
#             curr_sum += nums[i]
        
#         if curr_sum > max_sum:
#             max_sum = curr_sum
#             end_idx = i
    
#     return nums[start_idx:end_idx+1]
        