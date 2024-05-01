class TrieNode():
    def __init__(self):
        self.isEnd = False
        self.children = [None]*26
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if node.children[ord(char) - ord('a')] == None:
                node.children[ord(char) - ord('a')] = TrieNode()
            node = node.children[ord(char) - ord('a')]
        node.isEnd = True
                

    def search(self, word: str) -> bool:
        node = self.root
        def dfs(i, node):
            if i == len(word):
                return node.isEnd
            c = word[i]
            if c == ".":
                for child in node.children:
                    if child and dfs(i+1, child):
                        return True
            else:
                if node.children[ord(c) - ord('a')] and dfs(i+1, node.children[ord(c) - ord('a')]):
                    return True
            return False
        return dfs(0, node)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)