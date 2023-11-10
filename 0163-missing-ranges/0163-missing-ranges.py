class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        res = []
        if n < 1:
            res.append([lower, upper])
            return res
            
        if nums[0] != lower:
            res.append([lower, nums[0] - 1])
            
        for i in range(n - 1):
            if nums[i] + 1 != nums[i+1]:
                res.append([nums[i]+1, nums[i+1] - 1])
                
        if nums[-1] != upper:
            res.append([nums[-1]+1, upper])
            
        return res
        