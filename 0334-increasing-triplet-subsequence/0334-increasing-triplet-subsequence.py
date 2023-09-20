class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_smallest = float("inf")
        second_smallest = float("inf")
        for num in nums:
            if num <= first_smallest:
                first_smallest = num
            elif num > first_smallest and num <= second_smallest:
                second_smallest = num
            elif num > first_smallest and num > second_smallest:
                return True
        return False