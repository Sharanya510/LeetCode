class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes

        # Convert all time points to minutes
        minutes_list = [convert_to_minutes(time) for time in timePoints]

        # Sort the list of time points in minutes
        minutes_list.sort()

        # Initialize the minimum difference to a large number
        min_diff = float('inf')

        # Calculate the difference between each pair of consecutive time points
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])

        # Calculate the difference between the first and last time point in a circular manner
        # circular_diff = (1440 + minutes_list[0] - minutes_list[-1]) % 1440
        circular_diff = (1440 + minutes_list[0] - minutes_list[-1]) % 1440
        min_diff = min(min_diff, circular_diff)

        return min_diff
    
# TIME COMPLEXITY -- O(nlogn)
# SPACE COMPLEXITY -- O(n)