class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        temp = 0
        highest = 0
        res = []
        for candy in candies:
            temp = highest
            highest = max(temp, candy)
        for candy in candies:
            temp = candy + extraCandies
            res.append(temp >= highest)
        return res