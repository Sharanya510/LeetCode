class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if(flowerbed[i]==0 and self.helper(flowerbed, i)):
                flowerbed[i]=1
                n = n-1
                if n==0:
                    return True
        return n<=0
    def helper(self, flowerbed, i):
        if i==0:
            return len(flowerbed)==1 or flowerbed[i+1]==0
        
        if i==len(flowerbed)-1:
            return flowerbed[i-1]==0
        
        return flowerbed[i+1]==0 and flowerbed[i-1]==0
        
        
        
        
        
        
        
        
#         for i in range(len(flowerbed)-1):
#             if flowerbed[i] == 1 and flowerbed[i+1] == 0 or  flowerbed[i] == 0 and flowerbed[i+1] == 1:
#                 continue
#             if flowerbed[i] == 0 and flowerbed[i+1] == 0:
#                 if n > 0:
#                     n -= 1
#                     continue
#             if flowerbed[i] == 1 and flowerbed[i+1] == 1:
#                 if n > 0:
#                     n -= 1
#                     continue
#                 else:
#                     return False
#         print(n)
#         if n == 0:
#             return True
        
#         return False
                
                
# 0   0   1   0   1

                
                

                