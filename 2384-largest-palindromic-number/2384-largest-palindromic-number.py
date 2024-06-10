class Solution:
    def largestPalindromic(self, num: str) -> str:
        dic = Counter(num)
        choice = '9876543210'
        single = ''
        res = ''
        
		# first loop we can ignore '0'
        for i in choice:
            if i in dic and dic[i] % 2 == 1:
                single = max(single,i)
            res += i*(dic[i] // 2)
        
        res += single
        
        for i in choice[::-1]:
            if i in dic:
                res += i*(dic[i] // 2)
            
        return '0' if not res.strip('0') else res.strip('0')