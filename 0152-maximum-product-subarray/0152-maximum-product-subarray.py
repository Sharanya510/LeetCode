class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        currMin = 1
        currMax = 1
        res = float('-inf')
        
        for num in nums:
            temp = currMax*num
            currMax = max(currMax*num,currMin*num,num)
            currMin = min(temp,currMin*num,num)
            res = max(res,currMax)
        
        
        return res