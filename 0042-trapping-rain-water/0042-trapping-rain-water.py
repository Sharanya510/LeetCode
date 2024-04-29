class Solution:
    def trap(self, height: List[int]) -> int:
        # Case of empty height list
        if len(height) == 0:
            return 0
        ans = 0
        size = len(height)
        # Create left and right max arrays
        left_max, right_max = [0] * size, [0] * size
        # Initialize first height into left max
        left_max[0] = height[0]
        for i in range(1, size):
            # update left max with current max
            left_max[i] = max(height[i], left_max[i - 1])
        # Initialize last height into right max
        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            # update right max with current max
            right_max[i] = max(height[i], right_max[i + 1])
        # Calculate the trapped water
        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]
        # Return amount of trapped water
        return ans
        
        
        # APPROACH -- BRUTE FORCE
        # ans = 0
        # size = len(height)
        # for i in range(1, size - 1):
        #     left_max = 0
        #     right_max = 0
        #     for j in range(i, -1, -1):  # Search the left part for max bar size
        #         left_max = max(left_max, height[j])
        #     for j in range(i, size):  # Search the right part for max bar size
        #         right_max = max(right_max, height[j])
        #     ans += min(left_max, right_max) - height[i]
        # return ans