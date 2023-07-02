class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # TIME COMPLEXITY -- nlog(k) : log k is for heap complexity, insertion or deletion time and doing this for n elements, hence n log(k)
#         nums_hash =  {}
#         res = []
#         for i, n in enumerate(nums):
#             if n not in nums_hash:
#                 nums_hash[n] = 1
#             else:
#                 nums_hash[n] += 1
#         print(nums_hash)
        
#         heap = []
#         for key, value in nums_hash.items():
#             if len(heap) < k:
#                 heapq.heappush(heap, (value, key))
#             elif len(heap) >= k:
#                 if value> heap[0][0]:
#                     heapq.heappop(heap)
#                     heapq.heappush(heap, (value, key))
        
#         res = []
#         while heap:
#             value, key = heapq.heappop(heap)
#             res.append(key)
            
#         return res

        nums_hash= {}
        for num in nums:
            if num not in nums_hash:
                nums_hash[num]=1
            else:
                nums_hash[num]+=1
        s = sorted(nums_hash, key = lambda x:nums_hash[x], reverse = True)
        return s[:k]

            
                