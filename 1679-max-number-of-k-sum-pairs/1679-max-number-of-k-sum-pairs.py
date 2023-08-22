class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        length = 0
        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] + nums[right] == k:
                length += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
        return length
        
        
        
        
        
        
        
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == k:
        #             num1 = nums[i]
        #             num2 = nums[j]
        #             nums.remove(num1)
        #             nums.remove(num2)
        #             length += 1
        # return length

# 1   2   3   4
# i   j
# i       j
# i           j
                
        