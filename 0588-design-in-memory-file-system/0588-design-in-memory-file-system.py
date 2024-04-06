class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.content = ""
class FileSystem:

    def __init__(self):
        self.root = Node()
        
    def find(self, path):
        cur = self.root
        for i in path.split('/'):
            if not i: continue
            cur = cur.children[i]
        return cur
    
    def ls(self, path: str) -> List[str]:
        cur = self.find(path)
        if cur.content:
            return [path.split('/')[-1]]
        return sorted(cur.children)

    def mkdir(self, path: str) -> None:
        self.find(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.find(filePath)
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        return self.find(filePath).content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)