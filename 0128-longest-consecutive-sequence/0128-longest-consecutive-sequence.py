class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        length, longest = 1,1
        if not nums:
            return 0
        
        for n in nums_set:
            if n-1 not in nums_set:
                curr_num = n
                length = 1
                while n+1 in nums_set:
                    n += 1
                    length += 1
                    longest = max(longest, length)
        return longest 