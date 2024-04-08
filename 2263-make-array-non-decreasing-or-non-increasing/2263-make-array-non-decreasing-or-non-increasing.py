class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def calculateTotalAbsoluteDifference(nums):
            # Initialize a min heap and a variable to track the total difference
            minHeap, totalDifference = [], 0

            # Iterate over each number in the nums array
            for num in nums:
                # If the current number is smaller than the absolute of the heap's top element,
                # calculate the difference and add it to the totalDifference
                if minHeap and -minHeap[0] > num:
                    totalDifference += abs(num - (-heapq.heappop(minHeap)))
                    heapq.heappush(minHeap, -num)

                # Always push the current number onto the heap (as its negative)
                heapq.heappush(minHeap, -num)

            return totalDifference

        # Calculate the minimum total absolute difference by considering
        # both the original and the reversed nums array
        forwardDifference = calculateTotalAbsoluteDifference(nums)
        reverseDifference = calculateTotalAbsoluteDifference(nums[::-1])

        return min(forwardDifference, reverseDifference)
        