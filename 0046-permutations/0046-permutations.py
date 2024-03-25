class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.helper([],nums,set())
        return self.res
    
    def helper(self,temp,nums,unique):
        if len(temp)==len(nums):
            self.res.append(temp[:])
            return
        for i in range(len(nums)):
            if nums[i] in unique:
                continue
            unique.add(nums[i])
            temp.append(nums[i])
            self.helper(temp,nums,unique)
            temp.pop()
            unique.remove(nums[i])
        