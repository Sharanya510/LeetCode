class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        i = 0
        while i <= len(nums) - 1:
            if nums[i] == val:
                del nums[i]
            else:
                i = i+1
        return len(nums)