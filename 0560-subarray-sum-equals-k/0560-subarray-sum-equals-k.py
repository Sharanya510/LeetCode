class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        h = defaultdict(int)
        for num in nums:
            curr_sum += num
            if curr_sum == k:
                count += 1
            
            count += h[curr_sum - k]
            # print("Count is ",count)
            h[curr_sum] += 1
        return count

# 1   1   1
# 0
# 1   2   3
# count = 2
# 1:1 
# 2:1
# 3:1

