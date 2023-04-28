class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0:
            return 0
        product = 1
        i = count = 0
        for j in range(len(nums)):
            product *= nums[j]
            while product >= k and i <= j:
                product /= nums[i]
                i += 1
            count += j-i+1
        return count
                
        