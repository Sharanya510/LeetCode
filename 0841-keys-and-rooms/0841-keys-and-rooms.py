class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = [False]*len(rooms)
        q = deque()
        q.append(0)
        while q:
            curr = q.popleft()
            visit[curr] = True
            for v in rooms[curr]:
                if not visit[v]:
                    q.append(v)
        return all(visit)
        
        
        # for i, n in enumerate(rooms):
        #     # print(i,n)
        #     if (i+1) in n or (n == []) :
        #         continue
        #     else:
        #         return False
        # return True
                
        