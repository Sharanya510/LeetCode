class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        self.minimum = float("inf")
        
    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if len(self.min_stack) == 0 or val <= self.minimum:
            self.minimum = val
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.main_stack:
            value = self.main_stack[-1]
            if self.min_stack and value == self.min_stack[-1]:
                self.main_stack.pop()
                self.min_stack.pop()
            elif self.main_stack:
                self.main_stack.pop()
        if len(self.min_stack) == 0:
            self.minimum = float("inf")
        else:
            self.minimum = self.min_stack[-1]

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]

# main --> [ 2147483646, 2147483646, 2147483647 ]
# min --> [ 2147483646,  ]
        
        
        
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()