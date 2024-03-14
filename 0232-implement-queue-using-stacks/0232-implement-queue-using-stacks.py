class MyQueue:

    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        if len(self.first) == 0:
            self.front = x
        self.first.append(x)

    def pop(self) -> int:
        if len(self.second) == 0:
            while self.first:
                self.second.append(self.first.pop())
        return self.second.pop()

    def peek(self) -> int:
        if len(self.second) == 0:
            return self.front
        return self.second[-1]
    
    def empty(self) -> bool:
        return len(self.first) == 0 and len(self.second) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()