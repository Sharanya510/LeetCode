class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        res=[]
        res=sentence.split()
        dictionary.sort()
        #print(dictionary)
        for i in range(len(res)):
            for j in range(len(dictionary)):
                if res[i].startswith(dictionary[j]):
                    res[i]=dictionary[j]
                    break
        return " ".join(res)
        
       
            