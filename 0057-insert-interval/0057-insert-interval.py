class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if not intervals:
            return [newInterval]
        
        intervals.append(newInterval)
        intervals.sort()
        # print(intervals)
        res.append(intervals[0])
        i = 1
        while i < len(intervals):
            if intervals[i][0] > res[-1][1]:
                res.append(intervals[i])
                i = i + 1
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
                # print(res)
                i = i + 1
        return res
                
                