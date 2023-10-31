class TrieNode:
    def __init__(self, val):
        self.isEnd = False
        self.children = [None] * 26
        self.val = val
        
class Trie:
    def __init__(self):
        self.root = TrieNode(None)
        
    def insert(self, word):
        node = self.root
        for c in word:
            if node.children[ord(c) - ord('a')] == None:
                node.children[ord(c) - ord('a')] = TrieNode(c)
            node = node.children[ord(c) - ord('a')]
        node.isEnd = True
    
    def getSuggestions(self, searchword):
        node = self.root
        suggestions = []
        for c in searchword:
            if node.children[ord(c) - ord('a')] == None:
                return suggestions
            node = node.children[ord(c) - ord('a')]
        suggestions = self.dfs(node, searchword[:-1], "", [])
        return suggestions
    
    def dfs(self, node, prefix, path, res):
        if len(res) >= 3:
            return res
        
        path += node.val
        
        if node.isEnd:
            res.append(prefix + path[:])
        
        
        for child in node.children:
            if child != None:
                res = self.dfs(child, prefix, path[:], res)
        
        return res
        
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        res = []
        curr_searchword = ""
        
        for product in products:
            trie.insert(product)
        
        for c in searchWord:
            curr_searchword += c
            suggestions = trie.getSuggestions(curr_searchword)
            res.append(suggestions)
        return res
        
        