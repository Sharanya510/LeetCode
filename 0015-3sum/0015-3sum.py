class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            a = nums[i]
            k = i + 1
            j = len(nums) - 1
            while k < j:
                b = nums[k]
                c = nums[j]
                if a + b + c < 0:
                    k += 1
                elif a + b + c > 0:
                    j -= 1
                else:
                    if [a,b,c] not in res:
                        res.append([a,b,c])
                    k += 1
                    j -= 1
        return res
    
    