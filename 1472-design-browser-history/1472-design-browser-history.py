class BrowserHistory:

    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.browser_history = [homepage]

    def visit(self, url: str) -> None:
        if len(self.browser_history) < self.i + 2:
            self.browser_history.append(url)
        else:
            self.browser_history[self.i + 1] = url
        self.i += 1
        self.len = self.i +1 
            
    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.browser_history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.len - 1)
        return self.browser_history[self.i]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)