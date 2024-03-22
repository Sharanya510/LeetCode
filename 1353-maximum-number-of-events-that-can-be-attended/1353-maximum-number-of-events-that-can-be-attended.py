class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()
        start, end = float("inf"), float("-inf")
        for i,j in events:
            start = min(start,i)
            end = max(end,j)
        c, i, heap = 0, 0, []
        for day in range(start,end+1):
            while i < n and events[i][0] == day:
                heapq.heappush(heap,events[i][1])
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                c += 1
        return c
        