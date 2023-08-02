# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans=0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = None
        self.inorder(root)
        return self.ans
    
    
    def inorder(self, root):
        if not root:
            return None
        self.inorder(root.left)
        self.k -= 1
        if self.k == 0:
            self.ans=root.val
            return self.ans
        self.inorder(root.right)
        
        
        
        
        
        
        #ITERATIVE -- BFS
#         stack = []
#         prev = float("-inf")
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left
            
#             root = stack.pop()
#             if k > 0:
#                 k -= 1
#             if k == 0:
#                 return root.val
#             root = root.right
                
        
        # BRUTE -- FORCE DFS
#         res = []
#         self.helper(root, res)
#         return res[k-1]
    
#     def helper(self, root, res):
#         if not root:
#             return None
#         self.helper(root.left, res)
#         res.append(root.val)
#         self.helper(root.right,res)
#         return res
        
# in-order traversal --> left root right
# 1 null 2 3 4 null null
