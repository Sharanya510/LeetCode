class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_value = max_index = nums[0]
        min_index = max_value = 0
        for i, num in enumerate(nums):
            if num < min_value:
                min_index = i
                min_value = num
            if num >= max_value:
                max_index = i
                max_value = num
        return min_index + len(nums) - 1 - max_index - (min_index > max_index)
        # count = 0
        # N = len(nums) - 1
        # min_ele, max_ele = min(nums), max(nums)
        # min_index, max_index = nums.index(min_ele), nums.index(max_ele)
        # if max_index < min_index:
        #     return N - 1 - max_index + min_index - 1
        # else:
        #     return N - 1 - max_index + min_index
    
# 3   4   5   5   3   1
# min --> 5 --> length - index 0
# max --> 3 --> length - max_index

