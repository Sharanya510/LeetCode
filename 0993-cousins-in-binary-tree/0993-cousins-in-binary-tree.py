# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return None
        queue = deque()
        parent = None
        queue.append([root, parent])
        while queue:
            size = len(queue)
            foundone = False
            for i in range(size):
                node, par = queue.popleft()
                if node.val == x or node.val == y:
                    if not foundone:
                        foundone = True
                        parent = par
                    else: return parent != par
                if node.left:
                    queue.append([node.left, node])
                if node.right:
                    queue.append([node.right, node])
                
        return False

    
# [1,0, none]
# node = 1, level = 0, parent = none
# [2,1,1] [3,1,1]
# [4,2,2] [5,2,3]
                