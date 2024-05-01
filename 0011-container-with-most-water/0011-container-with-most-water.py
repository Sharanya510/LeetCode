class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
#         maxarea = 0
#         for left in range(len(height)):
#             for right in range(left + 1, len(height)):
#                 width = right - left
#                 maxarea = max(maxarea, min(height[left], height[right]) * width)

#         return maxarea

        left, right = 0, len(height) - 1
        maxArea = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxArea = max(area, maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
        
        
#         1,8,6,2,5,4,8,3,7
#           l             r
        
#         6*(1)=6
        
        
        
        