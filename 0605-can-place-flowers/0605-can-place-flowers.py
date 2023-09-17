class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and self.helper(flowerbed, i) :
                flowerbed[i] = 1
                n = n - 1
                if n <= 0:
                    return True
        return n <= 0
        
    def helper(self, flowerbed, i):
        if i == 0:
            return len(flowerbed) == 1 or flowerbed[i+1] == 0
        
        if i == len(flowerbed) - 1:
            return flowerbed[i-1] == 0
        
        return flowerbed[i+1] == 0 and flowerbed[i-1] == 0
        