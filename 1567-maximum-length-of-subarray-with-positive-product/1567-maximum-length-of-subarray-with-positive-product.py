class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        negative_count = 0
        first_negative_index = None
        zero_index = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                negative_count = 0
                first_negative_index = None
                zero_index = i
            elif nums[i] < 0:
                negative_count += 1
                if first_negative_index == None:
                    first_negative_index = i

            if negative_count & 1 == 0:
                max_len = max(max_len, i - zero_index)
            else:
                max_len = max(max_len, i - first_negative_index)

        return max_len
                 
# 1   -2  -3  4
# i
# m = 0
#     i
#     n = 1
#     f = 1
#     m = 0
#         i
#         n = 2
#         f = 1
#         m = 3
#             i
#             m = 4
        