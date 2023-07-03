class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxarea = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxarea = max(area, maxarea)
            if height[l] <= height[r]:
                l += 1
            # elif height[l] > height[r]:
            #     r -= 1
            else:
                # l += 1
                r -= 1
        
        return maxarea


        # BRUTE-- FORCE
        # maxarea = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = (j - i) * min(height[i],  height[j])
        #         maxarea = max(area, maxarea)
        # return maxarea
            
        