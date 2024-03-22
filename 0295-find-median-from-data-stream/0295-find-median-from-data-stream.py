class MedianFinder:

    def __init__(self):
        # Min heap for the higher half elements
        self.hi = []
        # Max heap for the lower half elements, we invert the values to use it as a max heap
        self.lo = []

    def addNum(self, num: int) -> None:
        # Add to max heap
        heapq.heappush(self.lo, -num)  # Invert the num to simulate max heap

        # Balancing step
        # Move the top element from lo to hi to maintain the order
        heapq.heappush(self.hi, -heapq.heappop(self.lo))

        
        # Maintain size property, ensure sizes of heaps differ at most by 1 element
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            # If lo has more elements, the median is in lo
            return -self.lo[0]  # Remember to invert back
        else:
            # If hi and lo are of the same size, median is the average of tops of hi and lo
            return (-self.lo[0] + self.hi[0]) / 2.0


# APPROACH -- BRUTEFORCE O(NLOGN)
# def __init__(self):
#     self.nums=[]

# def addNum(self, num: int) -> None:
#     self.nums.append(num)

# def findMedian(self) -> float:
#     self.nums.sort()
#     n=len(self.nums)
#     if n%2!=0:
#         return self.nums[floor(n/2)]
#     else:
#         return (self.nums[floor(n/2)]+self.nums[floor(n/2)-1])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()