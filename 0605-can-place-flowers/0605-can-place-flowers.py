class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left_plot = (i==0) or (flowerbed[i-1] == 0)
                empty_right_plot = (i==len(flowerbed)-1) or (flowerbed[i+1] == 0) 
                
                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    count += 1
                if count >= n:
                    return True
        return count>=n
        
        
        
        
        
#         if len(flowerbed) == 1 and flowerbed[0] == n:
#             return False
#         else:
#             return True
#         for i in range(len(flowerbed)-2):
#             if flowerbed[i] == 1:
#                 if flowerbed[i+1] == 0 and flowerbed[i+2] != 1:
#                     flowerbed[i+2] = 1
#                     n = n - 1
#             else:
#                 if flowerbed[i+1] == 1 and flowerbed[i+2] != 0:
#                     flowerbed[i+2] = 0
#                     n = n - 1
#                 if flowerbed[i+1] == 0 and flowerbed[i+2] != 0:
#                     flowerbed[i] = 1
#                     n = n - 1
           
#         return n == 0
               

               
                
            