import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        heapq.heappush(heap,nums[0])
        
        k -= 1
        for i in range(1,len(nums)):
            if heap and k>0:
                heapq.heappush(heap,nums[i])
                k-=1
            elif k<=0:
                if heap[0]<nums[i]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,nums[i])
        return heap[0]
                  
            
            
        
       
        