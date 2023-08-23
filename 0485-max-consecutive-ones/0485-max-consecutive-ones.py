class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # left = 0
        # length = 0
        # max_length = 0
        # for right in range(len(nums)):
        #     if nums[right] == 1:
        #         length += 1
        #     else:
        #         left = right 
        #         length = 0
        #     max_length = max(length, max_length)
        # return max_length
        left = 0
        length = 0
        max_length = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                length = right - left + 1
                max_length = max(length, max_length)
            else:
                left = right + 1 
                length = 0
            
        return max_length
    
    
    

# 1   1   0   1   1   1
# l
# r
# length = 1
#     r
#     length = 2
#         r
#         l
#         length = 0
#             r
#             length = 1
#                 r
#                 length = 2
#                         r
#                         length = 3
    
        