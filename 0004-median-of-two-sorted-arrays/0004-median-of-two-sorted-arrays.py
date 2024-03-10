class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_array = nums1 + nums2
        new_array.sort()
        # print(new_array)
        n = len(new_array)
        if n % 2 == 0:
            n = n // 2
            return (new_array[n-1] + new_array[n]) / 2
        else:
            n = n // 2
            return new_array[n]
            
# 1   2   3   4   5
