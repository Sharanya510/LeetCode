class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(i, res, temp, nums):
            if i == len(nums):
                res.append(list(temp))
                return
            dfs(i+1, res, temp + [nums[i]], nums)
            dfs(i+1, res, temp, nums)
        res = []
        temp = []
        dfs(0, res, temp, nums)
        return res