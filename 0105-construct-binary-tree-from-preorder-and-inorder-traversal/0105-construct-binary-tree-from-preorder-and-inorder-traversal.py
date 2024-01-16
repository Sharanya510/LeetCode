# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # APPROACH --> RECURSION
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(N)
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if root.val == inorder[i]:
                index = i
                break
        
        left_inorder = inorder[:index]
        right_inorder = inorder[index+1 : len(inorder)]
        left_preorder = preorder[1 : index+1]
        right_preorder = preorder[index+1 : len(preorder)]
        
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root