class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        left_sum, right_sum = 0, 0
        ans = 0
        while left < right:
            left_sum += nums[left]
            right_sum += nums[right]
            while left < right and left_sum != right_sum:
                if left_sum > right_sum:
                    right -= 1
                    right_sum += nums[right]
                    ans += 1
                else:
                    left += 1
                    left_sum += nums[left]
                    ans += 1
            left += 1
            right -= 1
        return ans
#         n = len(nums)
#         low, high, count = 0, n-1, 0
#         while low <= high:
#             if nums[low] == nums[high]:
#                 low += 1 
#                 high -= 1 
#             elif nums[low] < nums[high]:
#                 count += 1
#                 nums[low+1] += nums[low]
#                 low += 1
#             else:
#                 count += 1
#                 nums[high-1] += nums[high]
#                 high -= 1

#         return count
        
        # left, right = 0, len(nums)-1
        # count = 0
        # while left < right:
        #     if nums[left] > nums[right]:
        #         adj_sum = nums[right-1]+nums[right]
        #         if adj_sum == nums[left]:
        #             count +=1
        #             nums[right-1] = adj_sum
        #             del nums[right]
        #             right = right-1
        #         left += 1
        #         right -= 1
        # return count
                