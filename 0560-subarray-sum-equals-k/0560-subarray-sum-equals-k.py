class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # total, count = 0, 0
        # resul = {0:1}
        # for num in nums:
        #     total += num
        #     if total - k in resul:
        #         count += resul[total-k]
        #     if total not in resul:
        #         resul[total] = 1
        #     else:
        #         resul[total] = resul[total] + 1
        # return count
        
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return(count)