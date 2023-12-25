class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(" ")
        return len(s[-1])
        
        
        
        
        # end_pointer = len(s)
        # length = 0
        # while end_pointer > 0:
        #     end_pointer -= 1
        #     if s[end_pointer] != " ":
        #         length +=1
        #     elif length > 0:
        #         return length
        # return length
        