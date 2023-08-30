class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count_zeros = 0
        while i < len(nums):
            if nums[i] == 0:
                count_zeros += 1
            i += 1
        # print(count_zeros)
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                del nums[j]
            else:
                j += 1
        # print(nums)
        
        while count_zeros:
            nums.append(0)
            count_zeros -= 1
        return nums
        