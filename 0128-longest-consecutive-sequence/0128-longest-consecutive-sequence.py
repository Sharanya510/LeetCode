class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # brute-force
        # nums.sort()
        # length = 0
        # longest = 0
        # if len(nums) == 0:
        #     length = -1
        #     longest = -1
        # for i in range(len(nums)-1):
        #     if abs(nums[i+1] - nums[i]) == 1:
        #         length += 1
        #         longest = max(length, longest)
        #     else:
        #         length = 0
        # return longest + 1
        
        # optimized
        nums_set = set(nums)
        length, longest = 0, 0
        for n in nums:
            if (n - 1) not in nums_set:
                length = 1
                while (n + length) in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest
                
        