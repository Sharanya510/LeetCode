# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.pairs = []

    def get_height(self, root: TreeNode) -> int:
        # return -1 for null nodes
        if root is None:
            return -1
        
        # first calculate the height of the left and right children
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        
        # based on the height of the left and right children, obtain the height of the current (parent) node
        curr_height = max(left_height, right_height) + 1

        # collect the pair -> (height, val)
        self.pairs.append((curr_height, root.val))

        # return the height of the current node
        return curr_height

    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.pairs = []
        
        self.get_height(root)
        # print(self.pairs)
        # sort all the (height, val) pairs
        self.pairs.sort(key=lambda p: p[0])
        # print(self.pairs)
        solution = defaultdict(list)
        
        for height, val in self.pairs:
            solution[height].append(val)
        
        return [solution[height] for height in sorted(solution.keys())]
