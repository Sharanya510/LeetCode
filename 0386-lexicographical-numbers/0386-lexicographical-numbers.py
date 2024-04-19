class TrieNode:
    def __init__(self):
        self.child = {}
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,x):
        cur = self.root
        for i,c in enumerate(x):
            if x[:i+1] not in cur.child:
                cur.child[x[:i+1]] = TrieNode()
            cur = cur.child[x[:i+1]]
        

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        root = Trie()
    
        for i in range(1,n+1):
            root.insert(str(i))
        
        res = []

        def dfs(r):
            for x in r.child:
                res.append(int(x))
                dfs(r.child[x])
            
        dfs(root.root)

        return res
            
