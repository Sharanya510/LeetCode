class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, res, temp, nums):
            if i == len(nums):
                if temp not in res:
                    res.append(temp)
                return
            dfs(i+1, res, temp + [nums[i]], nums)
            dfs(i+1, res, temp, nums)
        res = []
        temp = []
        nums.sort()
        dfs(0, res, temp, nums)
        return res