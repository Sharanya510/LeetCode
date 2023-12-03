class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(i, temp, total):
            if total == target:
                res.append(list(temp))
                return
            if i >= len(candidates) or total > target:
                return
            temp.append(candidates[i])
            dfs(i, temp, total + candidates[i])
            temp.pop()
            dfs(i+1, temp, total)
        
        res = []
        temp = []
        dfs(0, temp, 0)
        return res