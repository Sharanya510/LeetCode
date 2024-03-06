class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return None
        path = []
        res = []
        self.helper(candidates, target, 0, path, res)
        return res
    
    def helper(self, candidates, target, i, path, res):
        if target < 0 or i == len(candidates):
            return
        if target == 0:
            res.append(path[:])
            return
       
        
#       without choosing element
        self.helper(candidates, target, i+1, path, res)
        path.append(candidates[i])
        
        self.helper(candidates, target-candidates[i], i, path, res)
        path.pop()