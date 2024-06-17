class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            # print(res)
            if n % 2 == 1:
                res <<= 1
                # print("res value before: " ,res)
                res += 1
                # print("res value before: " ,res)
            else:
                res <<= 1
            # print("n value before: " ,n)
            n >>= 1
            # print("n value after: " ,n)
        return res
    
    
        