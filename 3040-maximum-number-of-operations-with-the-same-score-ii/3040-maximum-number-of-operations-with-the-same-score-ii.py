class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        memory = {}
        def solve(nums,score,count) :
            if(len(nums) <= 1) :
                return count
            
            if (tuple(nums), score) in memory :
                return memory[(tuple(nums), score)]
            
            front = 0
            if(nums[0]+nums[1] == score) :
                front += solve(nums[2:],nums[0]+nums[1],count+1)
            last = 0
            if(nums[-1]+nums[-2] == score) :
                last += solve(nums[:-2],nums[-1]+nums[-2],count+1)
            combo = 0
            if(nums[0]+nums[-1] == score) :
                combo += solve(nums[1:-1],nums[0]+nums[-1],count+1)


            result = max(front,last,combo,count)
            memory[(tuple(nums), score)] = result
            return result

        return max(solve(nums[2:],nums[0]+nums[1],1),solve(nums[:-2],nums[-1]+nums[-2],1),solve(nums[1:-1],nums[0]+nums[-1],1))