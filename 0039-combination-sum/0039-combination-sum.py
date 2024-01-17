class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return []
        
        # quit if we went out of bounds
        if target < 0:
            return None
        out = []
        
        # two cases here:
        # if a candidate is the target add to solutions 
        # since everything after will be beyond the sum
        # if < target : get combinations on target-cur_candidate,
        # then merge each solution with the cur_candidate

        for i in range(len(candidates)):
            candidate = candidates[i]
            if candidate == target:
                out.append([candidate])

            if candidate < target:
                solutions = self.combinationSum(candidates[i:], target-candidate)
                for solution in solutions:
                    if solution is not None:
                        out.append([candidate, *solution])
        return out