# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.previous, self.inorder_successor_node = None, None
        # case 1 : lets say for a given node p, check if there exists a right child, if it exists then go till the last leftmost child because that will be the value greater than this value.
        if p.right:
            leftmost = p.right
            while leftmost.left:
                leftmost = leftmost.left
            self.inorder_successor_node = leftmost
        else:
            self.inorderCase2(root, p)
        return self.inorder_successor_node
    
    def inorderCase2(self, node: 'TreeNode', p: 'TreeNode'):
        if not node:
            return
        self.inorderCase2(node.left, p)
        if self.previous == p and not self.inorder_successor_node:
            self.inorder_successor_node = node
            return
        self.previous = node
        self.inorderCase2(node.right, p)
        