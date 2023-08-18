"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            temp = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
                temp.append(node.val)
            res.append(temp)
        return res
            
            