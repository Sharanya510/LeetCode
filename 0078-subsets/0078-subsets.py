class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, nums, res, temp):
            if i == len(nums):
                res.append(temp)
                return
            dfs(i+1, nums, res, temp + [nums[i]])
            dfs(i+1, nums, res, temp)
        res =[]
        temp = []
        dfs(0, nums, res, temp)
        return res