class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))

        # idx is the key used for comparing nodes in both heaps

        # lower_heap is a min heap for (idx, val) pairs
        lower_heap = []

        # upper_heap is a max heap for (idx, val) pairs
        upper_heap = []

        # keeps track of the minimum absolute differencce
        min_diff = float('inf')  
        
        for val, idx in sorted_nums:
            heapq.heappush(lower_heap, (idx, val)) 

            # NOTE: negating the keys of a min heap is equivalent to a max heap
            heapq.heappush(upper_heap, (-idx, val))

            # smallest index in the heap (i.e. the root) is more than x away from idx
            while len(lower_heap) > 0 and lower_heap[0][0] <= idx - x:
                # updates min_diff if the difference between val and the root's val is smaller
                min_diff = min(min_diff, val - heapq.heappop(lower_heap)[1])             
            
            # largest index in the heap (i.e. the root) is more than x away from idx
            while len(upper_heap) > 0 and upper_heap[0][0] <= -(x + idx):
                min_diff = min(min_diff, val - heapq.heappop(upper_heap)[1])      

        return min_diff