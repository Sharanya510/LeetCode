class Solution:
    def numWays(self, s: str) -> int:
        mod = 10**9 + 7
        ones = sum(map(int, s))

        # If the total number of ones is not divisible by 3, return 0.
        if ones % 3 != 0:
            return 0

        if ones == 0:
            # If there are no ones, the splits can only occur between zeros.
            # Choose 2 splits from n-1 positions (Combination: (n-1)C2).
            return ((len(s) - 1) * (len(s) - 2) // 2) % mod

        ones_per_partition = ones // 3
        ways_to_split_first = ways_to_split_second = 0
        ones_count = 0

        for bit in s:
            ones_count += int(bit)
            if ones_count == ones_per_partition:
                ways_to_split_first += 1
            elif ones_count == 2 * ones_per_partition:
                ways_to_split_second += 1

        # The total ways is the product of the ways to split at the two points.
        return (ways_to_split_first * ways_to_split_second) % mod
