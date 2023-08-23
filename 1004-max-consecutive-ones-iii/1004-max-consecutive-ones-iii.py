class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        maximum = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            maximum = max(maximum, right - left + 1)
        return maximum
            
#         length = 0
#         max_length = 0
#         temp = 0
#         for i in range(len(nums)):
#             if nums[i] == 1:
#                 length += 1
#             if nums[i] == 0 and temp <= k:
#                 length += 1
#                 temp += 1
#             if nums[i] == 0 and temp == k:
#                 length = 0
#             max_length = max(length, max_length)
#         return max_length
    


