class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ##keep track of max and min so far at every n, if n is 0 reset both to 1,1
        max_so_far,min_so_far=1,1
        result=max(nums)
        for n in nums:
            if n==0:
                max_so_far,min_so_far=1,1
                continue
            temp=n*max_so_far
            max_so_far=max(n,n*max_so_far,n*min_so_far)
            min_so_far=min(n,temp,n*min_so_far)
            result=max(result,max_so_far)
        return result
          
        
        