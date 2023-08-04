# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
# PREORDER --> root, left, right
# INORDER --> left, root, right
        if not preorder or not inorder:
            return 
        root = TreeNode(preorder[0])
        index = 0
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                index = i
                break
        left_inorder = inorder[0:index]
        left_preorder = preorder[1:index+1]
        right_preorder = preorder[index+1:len(preorder)]
        right_inorder = inorder[index+1:len(inorder)]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root

        
