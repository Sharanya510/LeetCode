class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxArea = max(area, maxArea)
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return maxArea