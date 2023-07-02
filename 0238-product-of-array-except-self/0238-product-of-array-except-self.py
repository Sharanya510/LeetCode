class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr=[1]*len(nums)
        right_arr=[1]*len(nums)
             
        product=1
        for i in range(len(nums)-1):
            product=product*nums[i]
            left_arr[i+1]=product
        # print(left_arr)
        
        product=1
        
        for i in range(len(nums)-2,-1,-1):
            product=product*nums[i+1]
            right_arr[i]=product
#         print(right_arr)
        
        ans=[]
        
        for i in range(len(nums)):
            ans.append(left_arr[i]*right_arr[i])
        return ans
           
        # SECOND APPROACH
#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
            
#         # print(res)
        
#         postfix = 1
#         for i in range(len(nums) - 1, -1 , -1 ):
           
#             res[i] *= postfix
#             postfix *= nums[i]
#         # print(res)
#         return res
            
            
            
