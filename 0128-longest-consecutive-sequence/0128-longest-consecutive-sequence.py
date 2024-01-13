class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length, longest = 1, 1
        nums_set = set(nums)
        for n in nums_set:
            if n -1 not in nums_set:
                length = 1
                while n + 1 in nums_set:
                    n = n +1
                    length += 1
                    longest = max(length, longest)
        return longest