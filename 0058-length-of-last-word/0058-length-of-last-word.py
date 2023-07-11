class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_string = s.strip()
        # print(s)
        # print(s.strip())
        res = []
        out = ""
        for i in range(len(new_string)):
            if new_string[i] == " " :
                res.append(out)
                out = ""
            elif i == len(new_string) - 1:
                out += new_string[i]
                res.append(out)
            else:
                out += new_string[i]
        return len(res[-1])
                
        