class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        dist = [math.inf] * n
        queue = deque()
        queue.append((src, 0))
        stops = 0
        while stops <= k and queue:
            size = len(queue)
            for _ in range(size):
                node, distance = queue.popleft()
                for neighbour, price in adj[node]:
                    if distance + price >= dist[neighbour]:
                        continue
                    dist[neighbour] = distance + price
                    queue.append((neighbour, dist[neighbour]))
            stops += 1
        return -1 if dist[dst] == math.inf else dist[dst]
