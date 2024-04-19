class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        current = 0
        st = []
        while current < len(height):
            # If current height is greater than the height of the bar at stack top,
            # it means we can potentially trap water.
            while st and height[current] > height[st[-1]]:
                top = st.pop()
                if not st:
                    break
                # Calculate the distance and the bounded height.
                distance = current - st[-1] - 1
                bounded_height = min(height[current], height[st[-1]]) - height[top]
                ans += distance * bounded_height
            st.append(current)
            current += 1
        return ans
        
        
        
        
#         ans = 0
#         size = len(height)
#         for i in range(1, size - 1):
#             left_max = 0
#             right_max = 0
            
#             # Search the left part for max bar size
#             for j in range(i, -1, -1):
#                 left_max = max(left_max, height[j])
            
#             # Search the right part for max bar size
#             for j in range(i, size):
#                 right_max = max(right_max, height[j])
            
#             # Calculate the trapped water at current bar
#             ans += min(left_max, right_max) - height[i]
#             # print(ans)
#         return ans