class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        ans = stack_ptr = 0
        for num in nums:
            while stack_ptr and num < nums[stack_ptr-1]:
                stack_ptr -= 1
            nums[stack_ptr] = num
            stack_ptr += 1
            ans += stack_ptr
        return ans