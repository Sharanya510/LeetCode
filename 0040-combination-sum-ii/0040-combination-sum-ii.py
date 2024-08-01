class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        candidates.sort()
        res = []
        self.helper(candidates, target, 0, [], res)
        return res
    
    def helper(self, candidates, target, start, path, res):
        if target == 0:
            res.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            
            path.append(candidates[i])
            self.helper(candidates, target - candidates[i], i + 1, path, res)
            path.pop()