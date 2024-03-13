class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        counts = [0] * (n + 1)
        
        for num in arr:
            counts[min(num, n)] += 1
        
        ans = 1
        for num in range(2, n + 1):
            ans = min(ans + counts[num], num)
    
        return ans
        
        
        
#         APPROACH --> BRUTE FORCE
#         TIME COMPLEXITY --> O(N log N)
#         SPACE COMPLEXITY --. O(1)
#         arr.sort()
#         ans = 1
#         for i in range(1, len(arr)):
#             if arr[i] >= ans + 1:
#                 ans += 1

#         return ans