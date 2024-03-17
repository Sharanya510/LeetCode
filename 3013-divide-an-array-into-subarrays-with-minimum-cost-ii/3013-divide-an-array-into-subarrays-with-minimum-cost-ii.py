# link to the problem: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/discuss/4605833/K-smallest-elements-in-Sliding-Window-w-SortedList-Detailed-Explanation

from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        window = SortedList()
        window_sum = 0
        ans = math.inf

        for end in range(1, n):
            incoming = nums[end]

            # removing leaving and adjust window_sum if necessary
            if len(window) >= dist + 1:
                upper = window[k - 2]
                leaving = nums[end - dist - 1]
                window.remove(leaving)
                new_upper = window[k - 2] if len(window) >= k - 1 else incoming 

                # leaving element contributes to current window sum
                if leaving <= upper:
                    window_sum -= leaving
                    window_sum += incoming if incoming < new_upper else new_upper

                # incoming element smaller than k-1th element
                elif incoming < upper:
                    window_sum -= upper
                    window_sum += incoming
            
            # if window size less than dist, add incoming to window sum if necessary
            elif len(window) < k - 1:
                window_sum += incoming
            elif k - 1 <= len(window) < dist + 1:
                upper = window[k - 2]
                if incoming < upper:
                    window_sum -= upper
                    window_sum += incoming
            
            window.add(incoming)
            if len(window) == dist + 1:
                ans = min(ans, window_sum)

        return ans + nums[0]