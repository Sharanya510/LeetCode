class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            a = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                b = nums[j]
                c = nums[k]
                if a + b + c >= target:
                    k -= 1
                elif a + b + c < target:
                    count += k - j
                    j += 1
                    print(a, b, c)
        return count

# [3,1,0,-2]
# 4

# 3   1   0   -2

# -2  0  1    3
# i   j       k --> 1 < 4 --> c = 1
# i   j   k     --> -1 < 4 --> c = 2
# i       j    k --> 2 < 4 --> c = 3