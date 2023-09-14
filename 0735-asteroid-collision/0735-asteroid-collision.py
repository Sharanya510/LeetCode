class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for asteroid in asteroids:
            flag=True
            while stack and stack[-1]>0 and asteroid<0:
                if abs(stack[-1])<abs(asteroid):
                    stack.pop()
                    continue
                elif abs(stack[-1])==abs(asteroid):
                    stack.pop()
                flag=False
                break
                
            if flag:
                stack.append(asteroid)
        return stack
        
        
        
        # res = {}
        # for i in range(len(asteroids)-1):
        #     for j in range(1, len(asteroids)):
        #         if asteroids[i] > 0 and asteroids[j] > 0 or asteroids[i] <0 and asteroids[j] < 0:
        #             res[i] = asteroids[i]
        #             res[j] = asteroids[j]
        #         elif asteroids[i] > 0 and asteroids[j] < 0:
        #             if abs(asteroids[i]) == abs(asteroids[j]):
        #                 continue
        #             if asteroids[i] > asteroids[j]:
        #                 res[i] = asteroids[i]
        #             else:
        #                 res[i] = asteroids[j]
        #         else:
        #             break;
        # return res.values()
    
        

            
        