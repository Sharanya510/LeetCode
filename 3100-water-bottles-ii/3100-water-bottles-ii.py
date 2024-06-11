class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        fullBottles = 0
        emptyBottles = numBottles
        BottlesDrink = numBottles
        while emptyBottles >= numExchange:
            fullBottles += 1
            emptyBottles -= numExchange
            numExchange += 1
            if fullBottles != 0 and emptyBottles < numExchange:
                emptyBottles += fullBottles
                BottlesDrink += fullBottles
                fullBottles = 0
        BottlesDrink += fullBottles
        return BottlesDrink
        
        
        
        # ans = e =  numBottles
        # while e >= numExchange:
        #     e -= (numExchange - 1)
        #     ans += 1
        #     numExchange += 1
        # return ans