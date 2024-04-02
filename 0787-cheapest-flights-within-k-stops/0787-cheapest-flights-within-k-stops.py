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
                # if node == dst:
                #     return min(dist[dst], distance)
                    # return distance
                # print(dist)
                for neighbour, price in adj[node]:
                    if distance + price >= dist[neighbour]:
                        continue
                    dist[neighbour] = distance + price
                    queue.append((neighbour, dist[neighbour]))
            stops += 1
        return -1 if dist[dst] == math.inf else dist[dst]
    
    
# graph = defaultdict(dict)
# for s, d, p in flights:
#     graph[s][d] = p
# q = deque([(src, 0)])
# steps = -1
# price = [float('inf')] * n
# price[src] = 0
# while q and steps < k:
#     for _ in range (len(q)):
#         node, prev_price = q.popleft()
#         for next_node in graph[node]:
#             new_price = prev_price + graph[node][next_node]
#             if new_price < price[next_node]:
#                 price[next_node] = new_price
#                 q.append((next_node, new_price))
#     steps += 1
# return price[dst] if price[dst] != float('inf') else -1
