class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.helper_rob(nums[1:]), self.helper_rob(nums[:-1]) )
    
    def helper_rob(self, nums):
        rob1, rob2 = 0, 0
        #[rob1, rob2, n, n+1 , ....]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
            