class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # APPROACH -- TOP DOWN -- RECURSIVE
        hash_map = {}
        def helper(index, total):
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (index, total) in hash_map:
                return hash_map[(index, total)]
            res = helper(index + 1, total - nums[index]) + helper(index+1, total + nums[index]) 
            hash_map[(index, total)] = res
            # print(hash_map)
            return res
        
        
        return helper(0, 0)
        
        # APPROACH -- BRUTE FORCE
        # def helper(index, total):
        #     if index == len(nums):
        #         if total == target:
        #             return 1
        #         else:
        #             return 0
        #     return helper(index+1, total + nums[index]) + helper(index + 1, total - nums[index])
        # return helper(0, 0)
        
        