class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
        
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
                
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        visited = set()
        res = set()
        obj = Trie()
        for word in words:
            obj.insert(word)
        
        rootNode = obj.root
    
        for i in range(rows):
            for j in range(cols):
                self.helper(board, obj.root, '', i, j, visited, res)
        return list(res)
    
    def helper(self, board, currNode, path, row, col, visited, res):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or (row, col) in visited:
            return
        
        ch = board[row][col]
        if currNode.children[ord(ch) - ord('a')] is None:
            return
        
        currNode = currNode.children[ord(ch) - ord('a')]
        
        if currNode.isEnd:
            res.add(path + ch)
            
        visited.add((row, col))
        
        self.helper(board, currNode, path + ch, row + 1, col, visited, res)
        self.helper(board, currNode, path + ch, row - 1, col, visited, res)
        self.helper(board, currNode, path + ch, row, col + 1, visited, res)
        self.helper(board, currNode, path + ch, row, col - 1, visited, res)
                
        visited.remove((row, col))

        
        
        
        
    