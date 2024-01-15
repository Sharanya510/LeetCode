class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area, max_area = 0, 0
        while left <= right:
            area = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(area, max_area)
        return max_area