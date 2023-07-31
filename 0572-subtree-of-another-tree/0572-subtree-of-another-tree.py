# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
# USING DFS
#         return self.dfs(root, subRoot)
    
#     def dfs(self, root, subRoot):
#         if root is None:
#             return False
#         elif self.is_identical(root, subRoot):
#             return True
#         return self.dfs(root.left, subRoot) or self.dfs(root.right, subRoot)
    
#     def is_identical(self, node1, node2):
#         if node1 is None or node2 is None:
#             return node1 is None and node2 is None
        
#         return ((node1.val == node2.val) and self.is_identical(node1.left, node2.left) and self.is_identical(node1.right, node2.right))
    
        
        # USING RECURSION
        if not subRoot:
            return True
        if not root:
            return False
        if self.helper(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    def helper(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.helper(p.left, q.left) and self.helper(p.right, q.right)
        return False