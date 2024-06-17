class Solution:
    def fib(self, n: int) -> int:
        # APPROACH -- DYNAMIC PROGRAMMING -- TOP DOWN -- RECURSIVE APPROACH
        if n < 2:
            return n
        memory = [0]*(n+1)
        memory[1] = 1
        memory[n] = self.fib(n-1) + self.fib(n-2)
        return memory[n]
        
        # APPROACH -- DYNAMIC PROGRAMMING -- BOTTOM UP -- ITERATIVE APPROACH
        # memory = [0] * (n+1)
        # if n < 2: 
        #     return n
        # memory[1] = 1
        # for num in range(2, n+1):
        #     memory[num] = memory[num-1] + memory[num-2]
        # return memory[num]

        
        # APPROACH 1
#         return self.helper(n)
    
#     def helper(self, n):
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         return self.helper(n-1) + self.helper(n-2)
        