class MedianFinder:

    def __init__(self):
        self.nums=[]

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n=len(self.nums)
        if n%2!=0:
            return self.nums[floor(n/2)]
        else:
            return (self.nums[floor(n/2)]+self.nums[floor(n/2)-1])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()