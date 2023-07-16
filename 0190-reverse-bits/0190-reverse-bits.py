class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
    
        for i in range(32):
            if n % 2 == 1:
                res <<= 1
                res += 1
            else:
                res <<= 1
            n >>= 1
        return res
    # 0011 > 0001 
    # 0000 > 0001 > 0011
    # 672 
    # 000 