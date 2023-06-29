class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        ans = []
        for i in range(len(nums) - 3):
            for k in range(i +1, len(nums) - 2):
                a = nums[i]
                b = nums[k]
                start = k + 1
                end = len(nums) - 1
                while start < end:
                    c = nums[start]
                    d = nums[end]
                    if a + b + c + d < target :
                        start += 1
                    elif a + b + c + d > target :
                        end -= 1
                    else:
                        res.append((a,b,c,d))
                        start += 1
                        end -= 1
        print(res)
        print(set(res))
        print(list(set(res)))
        for e in (set(res)):
            print(e)
            ans.append(list(e))
                        
        return ans
                    
                    
                
            
            