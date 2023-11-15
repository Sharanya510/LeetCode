class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_hashmap = Counter(p)
        counter = len(p_hashmap)
        start, end = 0, 0
        while(end < len(s)):
            char = s[end]
            if char in p_hashmap:
                p_hashmap[char] -= 1
                if p_hashmap[char] == 0:
                    counter -= 1
            while(counter == 0):
                if end - start + 1 == len(p):
                    res.append(start)
                ch = s[start]
                if ch in p_hashmap:
                    p_hashmap[ch] += 1
                    if p_hashmap[ch] > 0:
                        counter += 1
                start +=1
            end += 1
        return res
        
        