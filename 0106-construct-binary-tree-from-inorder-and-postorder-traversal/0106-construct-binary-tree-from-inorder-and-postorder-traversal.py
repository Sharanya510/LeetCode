# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#IN-ORDER --> left, root, right
# POST-ORDER --> left, right, root
        if not inorder or not postorder:
            return
        root = TreeNode(postorder[-1])
        index = 0
        
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                index = i
                break
        
        left_inorder = inorder[:index]
        left_postorder = postorder[:index]
        right_inorder = inorder[index+1:len(inorder)]
        right_postorder = postorder[index:len(postorder)-1]
        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)
        return root