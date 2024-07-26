import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[0])
        
        min_rooms = 0
         
        end_room_timings = []
        meeting_rooms = []
        
        for interval in intervals:
            current_start = interval[0]
            if min_rooms == 0 or end_room_timings[0] > current_start:
                min_rooms += 1 
                heapq.heappush(end_room_timings, interval[1])
            if end_room_timings[0] <= current_start:
                heapq.heappop(end_room_timings)
                heapq.heappush(end_room_timings, interval[1])
    
        return min_rooms
                