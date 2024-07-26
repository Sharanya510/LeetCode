class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.index = 0  # points to the current frequency in the encoding list
        self.remaining = 0  # remaining number of current value to exhaust

    def next(self, n: int) -> int:
        while self.index < len(self.encoding):
            if n <= self.encoding[self.index] - self.remaining:
                self.remaining += n
                return self.encoding[self.index + 1]
            else:
                n -= (self.encoding[self.index] - self.remaining)
                self.index += 2
                self.remaining = 0
        return -1



# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)