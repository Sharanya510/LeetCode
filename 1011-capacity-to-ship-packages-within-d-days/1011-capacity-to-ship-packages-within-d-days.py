class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.split_work(weights, mid) <= days:
                right = mid
            else:
                left = mid
        if self.split_work(weights, left) <= days:
            return left
        return right
        
    def split_work(self, weights, ship_size):
        work, days = 0, 0
        for weight in weights:
            if work + weight > ship_size:
                days += 1
                work = 0
            work += weight
        # print(days+1)
        return days + 1