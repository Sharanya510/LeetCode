# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return 
            if not node.left and not node.right:
                leaf_nodes.append(node)
            dfs(node.left)
            dfs(node.right)

        def construct_graph(node):
            if not node:
                return 
            if node.left:
                graph[node].add(node.left)
                graph[node.left].add(node)
            if node.right:
                graph[node].add(node.right)
                graph[node.right].add(node)
            construct_graph(node.left)
            construct_graph(node.right)

        def calculate_distance(root):
            stack, visited, count = [(root,0)], set([root]), 0
            while stack:
                node,dist = stack.pop(0)
                if node != root and not node.left and not node.right and dist <= distance:
                    count += 1 
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append((neighbor,dist+1))
                        visited.add(neighbor)
            return count

        leaf_nodes, graph = [], defaultdict(set)
        dfs(root)
        construct_graph(root)
        total = 0
        for i in leaf_nodes:
            total += calculate_distance(i)
        return total//2 