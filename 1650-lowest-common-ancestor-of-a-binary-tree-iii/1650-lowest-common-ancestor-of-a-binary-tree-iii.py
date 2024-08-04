"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def isChild(root, child):
            if not root: return False
            if root.left == child or root.right == child: return True
            return isChild(root.left, child) or isChild(root.right, child) 

        def helper(p, q):
            if not p and not q: return p
            if not p and q: return q
            if not q and p: return p
            if p == q: return p
            if isChild(p, q): return p
            if isChild(q, p): return q
            return helper(p.parent, q.parent)
        return helper(p, q)