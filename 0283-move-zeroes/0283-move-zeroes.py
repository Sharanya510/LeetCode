class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for n in nums:
            if n == 0:
                count += 1
        # print(count)
        
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
            else:
                i += 1
        # print(nums)
        
        i = 0
        while i < count:
            nums.append(0)
            i += 1
        return nums
        