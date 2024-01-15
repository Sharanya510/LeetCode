# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p,q))
        while queue:
            p_node, q_node = queue.popleft()
            if not self.check(p_node, q_node):
                return False
            if p_node:
                queue.append((p_node.left, q_node.left))
                queue.append((p_node.right, q_node.right))
        return True
    
    def check(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!= q.val:
            return False
        return True
        
        # approach --> recursion
        # time complexity --> o(n)
        # space complexity --> o(n)
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            