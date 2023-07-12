class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        
        len_a = len(a)
        len_b = len(b)
        max_len = max(len_a, len_b)
        
        carry = 0
        
        a = '0' * (max_len - len_a) + a
        b = '0' * (max_len - len_b) + b
        
        for i in range(max_len - 1, -1, -1):
            if a[i] == '1' and b[i] == '1':
                if carry == 0:
                    res = res + '0'
                    carry = 1
                else:
                    res = res + '1'
                    carry = 1
            elif a[i] == '0' and b[i] == '0':
                if carry == 0:
                    res = res + '0'
                    carry = 0
                else:
                    res = res + '1'
                    carry = 0
            elif a[i] == '0' or b[i] == '0':
                if carry == 0:
                    res = res + '1'
                    carry = 0
                else:
                    res = res + '0'
                    carry = 1
        if carry == 1:
            return '1'+ res[::-1]
        else:
            return res[::-1]
        