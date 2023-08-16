class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums):
            if left_sum == (S -left_sum - x):
                return i
            left_sum += x
        return -1
        
        # left = 0
        # right = len(nums)-1
        # left_sum = nums[left]
        # right_sum = nums[right]
        # while left < right:
        #     if left_sum < right_sum:
        #         left += 1
        #         left_sum += nums[left]
        #         # print(left_sum)
        #     elif left_sum > right_sum:
        #         right -= 1
        #         right_sum += nums[right]
        #     elif left_sum == right_sum:
        #         return left + 1
        # return -1    
            
# 1   7   3   6   5   6
# ls                  rs

# 1    2   3
# ls       rs

  
        