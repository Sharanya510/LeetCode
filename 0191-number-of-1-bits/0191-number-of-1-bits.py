class Solution:
    def hammingWeight(self, n: int) -> int:
        # BRUTE-FORCE METHOD 1
        # count = 0
        # while n != 0:
        #     temp = n % 2
        #     print(temp)
        #     if temp == 1:
        #         count += 1
        #     n = n // 2
        # return count
    
    
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count
        
        # BRUTE FORCE METHOD 2
        # n = bin(n)
        # count = 0
        # for c in n:
        #     if c == '1':
        #         count += 1
        #         print(count)
        # return count 
        