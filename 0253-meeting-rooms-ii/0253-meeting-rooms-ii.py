class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap=[]
        heapq.heappush(heap,intervals[0][1])
        for i in range(1,len(intervals)):
            if heap and heap[0]>intervals[i][0]:
                heapq.heappush(heap,intervals[i][1])
            elif heap and heap[0]<=intervals[i][0]:
                heapq.heappop(heap)
                heapq.heappush(heap,intervals[i][1])
        return len(heap)
    
        
        
        
        
        
        
        
        
#         res = []
#         intervals.sort()
#         if len(intervals) == 2 and intervals[0][1] > intervals[1][0]:
#             return len(intervals)
#         res.append(intervals[0])
        
#         # print(res)
#         for i in range(1, len(intervals)-1):
#             if res[-1][1] < intervals[i][0]:
#                 continue
#             elif intervals[i][1] == intervals[i+1][0]:
#                 res.append(intervals[i])
#             else:
#                 res.append(intervals[i])
#             print(res)
#         return len(res)