class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        ans = 0
        for num in nums:
            ans += counts[num]
            counts[num] += 1
        return ans
            
        
        
        
        
        
        # BRUTE -- FORCE
        # TIME COMPLEXITY -- O(n2)
        # total_pairs = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and i < j:
        #             total_pairs += 1
        # return total_pairs
        
        
        

        
# 1   2   3   1   1   3
# 0   1   2   3   4   5   
# 0,3
# 0,4
# 3,4
# 2,5