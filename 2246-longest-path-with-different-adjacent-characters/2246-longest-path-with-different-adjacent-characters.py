class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = collections.defaultdict(list)

        for i in range(1, len(parent)):
            tree[parent[i]].append(i)
  
        ans = 1
        def dfs(root):
            path_length_from_root = [1]
            for v in tree[root]:
                if s[root] != s[v]:
                     path_length_from_root.append(1+dfs(v))
                else:
                    dfs(v)
            path_length_from_root.sort(reverse = True)
            nonlocal ans
            if len(path_length_from_root) > 1:
                ans = max(ans, path_length_from_root[0] + path_length_from_root[1] -1)
            ans = max(ans, path_length_from_root[0])
            return path_length_from_root[0]
        dfs(0)
        return ans