class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(1, len(nums)+1, 1):
            res = res ^ i
            res = res ^ nums[i-1]
        return res
        
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i]!=i:
        #         return i
        # return len(nums)