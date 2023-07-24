class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for n in nums:
            if n not in hash_map:
                hash_map[n] = 1
            else:
                hash_map[n] += 1
        curr_key = 0
        curr_value = 0
        for key, value in hash_map.items():
            if value > curr_value:
                curr_key = key
                curr_value = value
        return curr_key
                
            
        
        
        
        
        # length, longest = 1, 0
        # num = 0
        # for i in range(len(nums) -1):
        #     for j in range(1, len(nums)):
        #         if nums[i] == nums[j] and i !=j:
        #             num = nums[j] 
        #             length += 1
        #             longest = max(longest, length)
        #             print(longest)
        # if longest >= num:
        #     longestnum = num
        # return longestnum
                