class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums[:] = [str(num) for num in nums]

        for i in range(len(nums)):
            for j in range(len(nums) - 1 - i):
                if int(nums[j] + nums[j + 1]) < int(nums[j + 1] + nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return str(int(''.join(nums)))
    
    
# 3   30  34  5   9
# i
# j
# 3 + 30 = 330
# 30 + 3 = 303
# i
#     j
#     30 + 34 = 3034
#     34 + 30 = 3430
#     3034 < 3430 --> swap
# 3   34  30  5   9
# i
#         j
#         30 + 5 = 305
#         5 + 30 = 530
#         305 < 530 --> swap
# 3   34  5   30  9
# i
#             j
#             30 + 9 = 309
#             9 + 30 = 930
#             309 < 930 --> swap
# 3   34  5   9   30
#     i
# j
# 3 + 34 = 334
# 34 + 3 = 343
# 334 < 343 --> swap
# 34  3   5   9   30
#     i
#     j
#     3 + 5 = 35
#     5 + 3 = 53
#     35 < 53 --> swap
# 34  5   3   9   30
#     i
#         j
#         3 + 9 = 39
#         9 + 3 = 93
#         39 < 93 --> swap
# 34  5   9   3   30
#     i
#             j
# 34  5   9   3   30
#         i
# j
# 34 + 5 = 345
# 5 + 34 = 534
# 345 < 543 --> swap
# 5   34  9   3   30
#         i
#     j
#     34 + 9 = 349
#     9 + 34 = 934
#     349 < 934 --> swap
# 5   9   34  3   30
#         i
#         j
# 5   9   34  3   30
#             i
# j
# 5 + 9 = 59
# 9 + 5 = 95
# 59 < 95 --> swap
# 9   5   34  3   30
# o/p --> 9534330