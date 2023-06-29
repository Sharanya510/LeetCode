class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_set = set(nums)
        longest = 1
        
        for n in hash_set:
            if (n - 1) not in hash_set:
                current_num = n
                length = 1
                
                while (n+ 1) in hash_set:
                    n += 1
                    length += 1
                    longest = max(longest, length)
        return longest
                    
        