class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        start = 0
        for end in range(len(s)):
            if end == len(s) - 1 or s[end] != s[end+1]:
                if end-start+1 >= 3:
                    res.append([start, end])
                start = end + 1
        return res
    
    
    
                
                