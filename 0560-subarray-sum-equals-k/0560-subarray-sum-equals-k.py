class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum, count = 0, 0
        hash = {0:1}
        for n in nums:
            sum += n
            if sum - k in hash:
                count = count + hash[sum-k]
            if sum not in hash:
                hash[sum] = 1
            else:
                hash[sum] = hash[sum]+ 1
        return count
        
        