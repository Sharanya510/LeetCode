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
            # with this line it is performing shallow copy, which means whatever is in the path, it gets reflected in the res and it is giving the empty array as output, this doesnt work
            # res.append(path)
            # inorder to avoid this, we need to do deep copy which means need to create an independent array that can store the combinations that we get from the path list into the res list, so the below code works
            res.append(path[:])
            return
       
      # without choosing element
        self.helper(candidates, target, i+1, path, res)
        path.append(candidates[i])
        # print(path)
        # with choosing element
        self.helper(candidates, target-candidates[i], i, path, res)
        path.pop()