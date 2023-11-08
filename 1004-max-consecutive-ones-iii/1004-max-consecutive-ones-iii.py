class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                while left <= right and k < 0:
                    if nums[left] == 0:
                        k += 1
                    left += 1
                
            max_length = max(max_length, right - left + 1)
        return max_length    
                
# 1   1   1   0   0   0   1   1   1   1   0
# l
# r
# length = 1
#     r
#     length = 2
#         r
#         length = 3
#             r
#             length = 4
#                 r
#                 length = 5
#                       r
#                       l
#                       length = 1
# 
                
            