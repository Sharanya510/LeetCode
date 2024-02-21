class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        max_length = 0
        for n in nums_set:
            length = 1
            if n - 1 not in nums_set:
                length = 1
                while (n + 1) in nums_set:
                    n = n + 1
                    length += 1
            max_length = max(length, max_length)
        return max_length
                    
        
# 100 -->
# 200 -->
# 1 --> 2 --> 3 --> 4