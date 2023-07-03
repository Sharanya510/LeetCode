class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s:
            if c.isalnum():
                res += c
            else:
                continue
        # print(res)
        rev_res = ""
        for i in range(len(res)-1, -1, -1):
            if res[i].isupper():
                rev_res += res[i].lower()
            else:
                rev_res += res[i]
        print(rev_res)
        
        new_res = rev_res[::-1]
        print(new_res)
        return rev_res == new_res
                
                
                
                
            
            
        