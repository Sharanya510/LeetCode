class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, res, temp, nums):
            if i == len(nums):
                res.append(temp)
                return
            dfs(i+1, res, temp + [nums[i]], nums)
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i = i +1
            dfs(i+1, res, temp, nums)
        res = []
        temp = []
        nums.sort()
        dfs(0, res, temp, nums)
        return res