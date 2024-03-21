class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0]*len(nums1)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    number = nums2[j]
                    for k in range(j, len(nums2)):
                        if nums2[k] > number:
                            ans[i] = nums2[k]
                            break
                        else:
                            ans[i] = -1
        return ans