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
        parent=None
        queue.append([root,parent])
       
        while queue:
            size = len(queue)
            flag = False
            for i in range(size):
                node, parent = queue.popleft()
                if node.val == x or node.val == y:
                    if not flag:
                        flag=True
                        x_parent=parent
                    else:
                        return x_parent!=parent               
                if node.left:
                    queue.append([node.left,node])
                if node.right:
                    queue.append([node.right,node])
        return False
    