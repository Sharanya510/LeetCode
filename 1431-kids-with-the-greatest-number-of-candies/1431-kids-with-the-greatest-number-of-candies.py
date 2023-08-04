class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        highest = max(candies)
        for candy in candies:
            res.append(candy + extraCandies >= highest)
        return res
        
        
        
        # BRUTE--FORCE
        # temp = 0
        # highest = 0
        # res = []
        # for candy in candies:
        #     temp = highest
        #     highest = max(temp, candy)
        # for candy in candies:
        #     temp = candy + extraCandies
        #     res.append(temp >= highest)
        # return res