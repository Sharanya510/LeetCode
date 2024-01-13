class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        heap = []
        for key, value in hash_map.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            elif len(heap) >= k :
                if value > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (value, key))
        
        res = []
        for value, key in heap:
            res.append(key)
        return res