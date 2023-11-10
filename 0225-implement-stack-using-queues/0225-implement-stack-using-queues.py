class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        
    def push(self, x: int) -> None:
        # if len(self.queue1) == 0:
        #     self.queue1.append(x)
        self.queue1.append(x)
        print(self.queue1)
        self.last_element = self.queue1[-1]

    def pop(self) -> int:
        if len(self.queue2) == 0:
            while self.queue1:
                self.queue2.append(self.queue1.pop(0))
        else:
            while self.queue1:
                self.queue2.append(self.queue1.pop(0))
        return self.queue2.pop()

    def top(self) -> int:
        if len(self.queue2) != 0:
            return self.queue2[-1]
        return self.last_element

    def empty(self) -> bool:
        return (len(self.queue1) == 0 and len(self.queue2) == 0)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()