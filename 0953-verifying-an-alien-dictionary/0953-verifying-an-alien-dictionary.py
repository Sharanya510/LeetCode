class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map={}
        for i in range(len(order)):
                order_map[order[i]]=i
        
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
                    
            for j in range(len(word1)):
                if j >= len(word2):
                    return False
                
                if word1[j]!=word2[j]:
                    if order_map[word1[j]]<order_map[word2[j]]:
                        break
                    else:
                        return False
                elif word1[j]==word2[j]:
                    continue
        return True
    
                