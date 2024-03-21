class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_stack = []
        my_hashmap = {}
        
        for num in nums2:
            while my_stack and num > my_stack[-1]:
                my_hashmap[my_stack.pop()] = num
            my_stack.append(num)
        
        while my_stack:
            my_hashmap[my_stack.pop()] = -1
            
        res = []
        for num in nums1:
            res.append(my_hashmap.get(num, -1))
        return res
            
        
        
        
        # ans = [0]*len(nums1)
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             number = nums2[j]
        #             for k in range(j, len(nums2)):
        #                 if nums2[k] > number:
        #                     ans[i] = nums2[k]
        #                     break
        #                 else:
        #                     ans[i] = -1
        # return ans