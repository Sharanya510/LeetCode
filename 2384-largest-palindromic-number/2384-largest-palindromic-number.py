from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        frequency = {}
        largestOdd = float("-inf")
        evens = [] #(value, frequency)
        res = []
        
        for n in num:
            if int(n) not in frequency:
                frequency[int(n)] = 0
            frequency[int(n)] += 1
            
        for key in frequency:
            if key > largestOdd and frequency[key]%2 == 1:
                largestOdd = key
        
        for key in frequency:
            if frequency[key] > 1:
                evens.append((key, frequency[key]))
        evens.sort()
        
        if largestOdd != float('-inf'):
            res.append(str(largestOdd))

        for num, freq in evens:
            if num == 0 and len(evens) == 1:
                break
            for i in range(freq//2):
                res.insert(0, str(num))
                res.append(str(num))
                
        if not res:
            return "0"
        return "".join(res)
