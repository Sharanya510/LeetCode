class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # Find the first element in sub that is greater than or equal to num
                i = 0
                while num > sub[i]:
                    i += 1
                sub[i] = num
        return len(sub)
    
#         dp = [1] * len(nums)
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)

#         return max(dp)

# 0   1   2   3   4   5   6
# 1   1   1   1   1   1   1
# 9   1   4   2   3   3   7
#     i
# j
# 1 > 9 - false
#         i
# j
# 4 > 9 - false
#     j
#     4>1 - true
#     dp[2] = max(1, 1+1) = 2
#              i
# j
# 2> 9 - false
#     j
#     2 > 1 - true
#     dp[3] = max(1 , 2) = 2
#           j 
#           2 > 4 - false
# 0   1   2   3   4   5   6
# 1   1   1   1   1   1   1
# 9   1   4   2   3   3   7
#                 i
# j
# 3 > 9 - false
#     j
#     3 > 1 - true
#     dp[4] = max(1, 2) = 2
#         j
#         3 > 4 - false
#             j
#             3 > 2 - true
#             dp[4] = max(2, 1 + 2) = 3
# 0   1   2   3   4   5   6
# 1   1   1   1   1   1   1
# 9   1   4   2   3   3   7
#                     i
# j
# 3 > 9 - false
#     j
#     3> 1 - true
#     dp[1] = max(1, 1+1) = 2
#         j
#         3 > 4 - false
#             j
#             3 > 2 - true
#             dp[5] = max(2, 1 + 2) = 3
#                   j
#                   3>3  -false
# 0   1   2   3   4   5   6
# 1   1   1   1   1   1   1
# 9   1   4   2   3   3   7
#                         i
# j
# 7 > 9 - false
#     j
#     7>1 - true
#     dp[6] = max(1, 1+2) = 3
#          7 > 4 - true
#          dp[6] = max(3, 1 + 2) = 3
#               j
#               7 > 2 - true
#               dp[6] = max(3, 1 + 2) = 3
#                   j
#                   7 > 3 - true
#                   dp[6] = max(3, 1 + 3) = 4