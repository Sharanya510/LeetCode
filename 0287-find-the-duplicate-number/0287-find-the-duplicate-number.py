class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Find the "entrance" to the cycle.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
    
#     1   3   4   2   2
#     0   1   2   3   4
    
#     slow = fast = 1
#     slow = nums[1] = 3
#     fast = nums[nums[1]] = nums[3] = 2
#     next itertion
#     slow = nums[3] = 2
#     fast = nums[nums[2]] = nums[4] = 2
#     slow == fast:
#         break
        
#     slow = 1
#     slow = nums[1] = 3
#     fast = nums[2] = 4
#     next iteration
#     slow = nums[3] = 2
#     fast = nums[4] = 2
#     return slow 