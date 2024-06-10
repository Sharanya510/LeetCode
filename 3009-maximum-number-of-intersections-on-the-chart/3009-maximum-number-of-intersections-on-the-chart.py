class Solution:
    def maxIntersectionCount(self, y: List[int]) -> int:
        events = {}
        N = len(y)
        for i,x in enumerate(y):
            if x not in events:
                events[x] = [0,0]
            if i == 0:
                if y[0] > y[1]:
                    events[x][1] -= 1
                else:
                    events[x][0] += 1
            elif i == len(y) - 1:
                if y[N-2] > y[N-1]:
                    events[x][0] += 1
                else:
                    events[x][1] -= 1
            else:
                if y[i] > y[i-1] and y[i] > y[i+1]:
                    events[x][0] -= 1
                    events[x][1] -= 1
                elif y[i] < y[i-1] and y[i] < y[i+1]:
                    events[x][0] += 1
                    events[x][1] += 1
        ys = sorted(list(set(y)))
        res = 0
        curr = 0
        for coor in ys:
            curr += events[coor][0]
            res = max(res,curr)
            curr += events[coor][1]
            res = max(res,curr)
        return res