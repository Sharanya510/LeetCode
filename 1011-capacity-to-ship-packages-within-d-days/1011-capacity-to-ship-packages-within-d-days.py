class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        res = high

        def CanShip(mid):
            ships, capacity = 1, mid
            for w in weights:
                if capacity - w < 0:
                    ships += 1
                    capacity = mid
                capacity -= w
            return ships <= days
            
                    
        while low <= high :
            mid = (low + high) // 2
            if CanShip(mid):
                res = min(mid, res)
                high = mid - 1
            else:
                low = mid + 1
        return res
        
            