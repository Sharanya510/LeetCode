class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        word = ""
        i, j = 0, 0
        length = 0
        while i < len(s):
            if i <= j and s[j] == "#":
                length = int(s[i:j])
                word = s[j+1: j+1+length]
                j = j+1+length
                i = j
                res.append(word)
            j += 1
            
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))