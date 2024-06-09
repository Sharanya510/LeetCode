class MinStack:

    def __init__(self):
        self.my_stack = []
        self.min_stack = []
        self.minValue = float("inf")

    def push(self, val: int) -> None:
        if len(self.my_stack) == 0 and len(self.min_stack) == 0:
            self.minValue = val
            self.min_stack.append(val)
        else:
            self.minValue = min(val, self.min_stack[-1])
            self.min_stack.append(self.minValue)
        self.my_stack.append(val)

    def pop(self) -> None:
        if len(self.my_stack) > 0 and len(self.min_stack) > 0:
            self.my_stack.pop()
            self.min_stack.pop()
        else:
            return null

    def top(self) -> int:
        if len(self.my_stack) != 0:
            return self.my_stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) != 0:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()