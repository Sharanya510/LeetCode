class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if node.children[ord(char) - ord('a')] == None:
                node.children[ord(char) - ord('a')] = TrieNode()
            node = node.children[ord(char) - ord('a')]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if node.children[ord(char) - ord('a')] != None:
                node = node.children[ord(char) - ord('a')]
            else:
                return False
            
        if node.isEnd == True:
            return True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if node.children[ord(char) - ord('a')] != None:
                node = node.children[ord(char) - ord('a')]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)