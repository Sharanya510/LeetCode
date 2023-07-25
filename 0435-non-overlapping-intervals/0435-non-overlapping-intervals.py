class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
#         print(intervals)
#         ans = 0
#         k = -inf
        
#         for x, y in intervals:
#             if x >= k:
#                 # Case 1
#                 k = y
#             else:
#                 # Case 2
#                 ans += 1
        
#         return ans
    
    
    
        length = 0
        # intervals.sort()
        # print(intervals)
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] > intervals[i+1][0]:
                length += 1
                intervals.remove(intervals[i+1])
                # print(intervals)
            else:
                i += 1
        return length
        