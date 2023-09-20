class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        s = s.strip()
        temp = s.split(" ")
        for word in temp:
            if word != "":
                res.append(word)
        
        # print(res)
        return " ".join(res[::-1])
           
        
        