class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        counts = {}
        for row, column in reservedSeats:
            if row not in counts:
                # We have 3 seats of each row
                counts[row] = [True, True, True]

            if  2 <= column <= 5:
                counts[row][0] = False
            
            if  4 <= column <= 7:
                counts[row][1] = False

            if  6 <= column <= 9:
                counts[row][2] = False

        ans = 0
        for key, value in counts.items():
            first, second, third = value
            if not second:
                ans += max(int(first), int(third))
            else:
                if first and third:
                    ans += 2
                else:
                    ans += 1

        return ans + (n - len(counts))*2