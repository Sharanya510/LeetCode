class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        
        leaves = []
        adj_list = defaultdict(list)
        for edge in edges:
            adj_list[edge[1]].append(edge[0])
            adj_list[edge[0]].append(edge[1])
        # print(adj_list)
        
        for i in adj_list:
            if len(adj_list[i]) == 1:
                leaves.append(i)
        # print(leaves)
        
        remaining_nodes = n
        
        while remaining_nodes > 2:
            new_leaves = []
            remaining_nodes -= len(leaves)
            while leaves:
                leaf = leaves.pop()
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves

# neighbors = {0 : [1], 1: [0,2,3], 2 : [1], 3: [1]}     
# leaves = [0, 2, 3]
# remaining_nodes = 4
# while loop:
#     remaining_nodes = 4-3 = 1
#     new_leaves = []
#     step 1:
#         leaf = 0
#         neighbor = 1
#         neighbors = {0 : [1], 1: [2,3], 2 : [1], 3: [1]}
#         len not equal to 1
#     step 2:
#         leaf = 2
#         neighbor = 1
#         neighbors = {0 : [1], 1: [3], 2 : [1], 3: [1]}
#         len = 1
#         new_leaves = [1]
#     step 3:
#         leaf = 3
#         neighbor = 1
#         neighbors = {0 : [1], 1: [], 2 : [1], 3: [1]}
#         len not equal to 1
        
