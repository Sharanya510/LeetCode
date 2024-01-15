# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        my_stack = []
        while True:
            while root:
                my_stack.append(root)
                root = root.left
            root = my_stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
        
        # APPROACH --> RECURSIVE INORDER TRAVERSAL
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(N)
#         res = []
#         self.inorder(root, res)
#         return res[k-1]
    
#     def inorder(self, root, res):
#         if not root:
#             return None
#         self.inorder(root.left, res)
#         res.append(root.val)
#         self.inorder(root.right, res)
#         return res