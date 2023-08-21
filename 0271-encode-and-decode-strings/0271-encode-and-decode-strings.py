class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res=""
        for string in strs:
            res+=str(len(string))+'#'+string
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res=[]
        i,j=0,0
        length=0
        while i < len(s):
            while j<len(s) and s[j]!='#':
                j+=1
            if j==len(s):
                return res
            length=int(s[i:j])
            res.append(s[j+1:j+1+length])
            j=j+length+1
            i=j
        return res
                
                
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))