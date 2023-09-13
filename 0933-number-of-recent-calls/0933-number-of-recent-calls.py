class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        
        while self.queue and self.queue[0] < self.queue[-1] - 3000:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)