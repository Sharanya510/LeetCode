class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxarea = 0
        while l < r:
            if height[l] < height[r]:
                
                area = (r - l) * min(height[l], height[r])
                maxarea = max(area, maxarea)
                l += 1
            elif height[l] > height[r]:
                area = (r - l) * min(height[l], height[r])
                maxarea = max(area, maxarea)
                r -= 1
            else:
                area = (r - l) * min(height[l], height[r])
                maxarea = max(area, maxarea)
                l += 1
                r -= 1
        
        return maxarea
#  0 1 2 3 4 5 6 7 8       
# [1,8,6,2,5,4,8,3,7]
# first --> l = 0, r = 8 --> area = (8-0)* min(1,7) = 8
# second--> l = 1, r = 8 --> area = (8-1)* min(7,8) = 49
# third--> l = 1, r = 7 --> area = (7-1)* min(8,3) = 18
# fourth--> l = 1, r = 6 --> area = (6-1)* min(8,8) = 40


        # BRUTE-- FORCE
        # maxarea = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         area = (j - i) * min(height[i],  height[j])
        #         maxarea = max(area, maxarea)
        # return maxarea
            
        