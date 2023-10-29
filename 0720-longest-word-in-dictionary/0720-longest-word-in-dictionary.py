class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26
        self.word = ""
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            if node.children[ord(c) - ord('a')] == None:
                node.children[ord(c) - ord('a')] = TrieNode()
            node = node.children[ord(c) - ord('a')]
        node.isEnd = True
        node.word = word
        
    def bfs(self):
        node = self.root
        queue = deque()
        queue.append(node)
        res = ''
        while queue:
            curr = queue.popleft()
            for n in curr.children:
                if n != None:
                    # print(n)
                    if n.isEnd:
                        queue.append(n)
                        if len(n.word) > len(res) or n.word < res:
                            res = n.word
        return res
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        return trie.bfs()
        
        
        
        
        
        # BRUTE -- FORCE
        # words.sort()
        # seen = set([""])
        # ans = ""
        # for word in words:
        #     if word[:-1] in seen:
        #         seen.add(word)
        #         if len(word) > len(ans):
        #             ans = word
        # return ans
            