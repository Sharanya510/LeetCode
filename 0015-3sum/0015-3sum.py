class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=set()
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    res.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
        out=[]
        for item in res:
            out.append(item)
        return out
            
     
        