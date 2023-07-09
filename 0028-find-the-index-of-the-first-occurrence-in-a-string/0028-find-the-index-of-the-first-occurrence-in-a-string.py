class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        
        if len(haystack) < len(needle):
            return -1
        
        if needle in haystack:
            i , j = 0, 0
            firstIndex = None
            
            while i < len(haystack) and j < len(needle):
                
                if haystack[i] == needle[j]:
                    if firstIndex is None:
                        firstIndex = i
                    j += 1
                    
                else:
                    if firstIndex is not None:
                        i = firstIndex
                    j = 0
                    firstIndex = None
                i += 1
            return firstIndex
            
            
            
        return -1
        