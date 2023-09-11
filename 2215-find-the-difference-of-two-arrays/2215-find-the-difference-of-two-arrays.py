class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[], []]
        for n in nums1:
            if n not in nums2 and n not in res[0]:
                res[0].append(n)
        for n in nums2:
            if n not in nums1 and n not in res[1]:
                res[1].append(n)
        return res