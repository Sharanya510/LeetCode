class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)

        return -heapq.heappop(stones) if stones else 0
        
        
        # APPROACH --> ARRAY BASED SIMULATION
#         def remove_largest():
#             index_of_largest = stones.index(max(stones))
#             # Remove largest stone
#             return stones.pop(index_of_largest)

#         while len(stones) > 1:
#             stone_1 = remove_largest()
#             stone_2 = remove_largest()
#             if stone_1 != stone_2:
#                 stones.append(stone_1 - stone_2)

#         return stones[0] if stones else 0