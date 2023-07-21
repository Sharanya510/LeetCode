class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(n):
        #     nums1[i+m] = nums2[i]
        # nums1.sort()
        
        p1 = m -1
        p2 = n -1
        i = m+n-1
        while p1 >=0 and p2 >=0:
                if nums1[p1] < nums2[p2]:
                    print(nums1)
                    nums1[i] = nums2[p2]
                    p2 -= 1
                    i -= 1
                elif nums1[p1] == nums2[p2]:
                    print(nums1)
                    nums1[i] = nums1[p1]
                    nums1[i-1] = nums2[p2]
                    p1 -=1
                    p2 -=1
                    i -= 2
                else:
                    print(nums1)
                    nums1[i] = nums1[p1]
                    p1 -=1
                    i -= 1
        # while p1 >=0 and p2 == 0:
        #     nums1[i] = nums1[p1]
        #     p1-=1
        #     i-=1
        while p2 >=0:
            nums1[i] = nums2[p2]
            p2 -= 1
            i-=1
        while p1 >=0 :
            nums1[i] = nums1[p1]
            p1 -= 1
            i-=1
        return nums1
#         p1          i
# 4   5   6   0   0   0
# 1   2   3
#         p2
    
    
         
        

            