class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = e =  numBottles
        while e >= numExchange:
            e -= (numExchange - 1)
            ans += 1
            numExchange += 1
        return ans