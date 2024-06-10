class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        q = deque()
        q.append((x, 0))
        seen = {x}
        while q:
            x, step = q.popleft()
            if x == y:
                return step
            if x % 11 == 0 and x // 11 not in seen:
                q.append((x // 11, step + 1))
                seen.add(x // 11)
            if x % 5 == 0 and x // 5 not in seen:
                q.append((x // 5, step + 1))
                seen.add(x // 5)
            if x + 1 not in seen:
                q.append((x + 1, step + 1))
                seen.add(x + 1)
            if x - 1 not in seen:
                q.append((x - 1, step + 1))
                seen.add(x - 1)