class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        heapq.heappush(heap, intervals[0][1])
        for i in range(1, len(intervals)):
            if heap and heap[0] > intervals[i][0]:
                heapq.heappush(heap, intervals[i][1])
            elif heap and heap[0] <= intervals[i][1]:
                heapq.heappop(heap)
                heapq.heappush(heap, intervals[i][1])
        return len(heap)
        