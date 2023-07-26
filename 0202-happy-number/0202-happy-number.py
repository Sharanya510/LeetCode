class Solution:
    def isHappy(self, n: int) -> bool:
        
        def recur(n):
            res = 0
            while n:
                temp = n % 10
                n = n // 10
                res += temp * temp
            return res
        
        hash_set = set()
        while n!=1 and n not in hash_set:
            hash_set.add(n)
            n = recur(n)
        return n == 1

            
        