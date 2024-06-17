class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: List[int]) -> int:
        t1 = 0
        t2 = 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp

        return t1
    
# 1   2   3   1
# 0   1   2   3
# max([1, 2, 3], [2, 3, 1])

# 1, 2, 3
# t1
# t2
# curr
# temp = 1
# t1 = 1+0 = 1
# t2 = 1

# curr = 2
# temp = 1
# t1 = max(2 + 1, 1) = 3
# t2 = 1

# curr = 3
# temp = 3
# t1 = max(3 + 1, 3) = 4
# t2 = 3
