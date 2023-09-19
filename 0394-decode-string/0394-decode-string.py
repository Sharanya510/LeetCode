class Solution:
    def decodeString(self, s: str) -> str:
        my_stack = []
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                prev = 0
                if i>0 and s[i-1].isdigit():
                    prev = int(my_stack.pop())*10
                my_stack.append(prev+int(c))
            if c == '[':
                my_stack.append(c)
            if c.isalpha():
                my_stack.append(c)
            if c == ']':
                str1 = ""
                while True :
                    c = my_stack.pop()
                    if c=='[':
                        break
                    str1 += c
                num = my_stack.pop()
                str2 = ""
                for i in range(int(num)):
                    str2 += str1
                my_stack.append(str2)
        res = ""
        while len(my_stack):
            res += my_stack.pop()
        return res[::-1]
                
        