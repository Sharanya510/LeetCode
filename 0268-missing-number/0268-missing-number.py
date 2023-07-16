class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # int res=0
        # for i in range(1, len(nums)+1, 1):
        #     res
        
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)