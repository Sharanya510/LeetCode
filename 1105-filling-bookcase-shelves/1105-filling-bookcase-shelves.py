class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # Initialize dp array with a large number
        dp = [float('inf')] * (len(books) + 1)
        dp[0] = 0  # Base case: no books, no height needed

        # Iterate over the books
        for i in range(1, len(books) + 1):
            width = 0
            max_height = 0

            # Check all possible positions for the last shelf that ends at book i
            for j in range(i, 0, -1):
                width += books[j - 1][0]  # Add the width of the book at position j-1
                max_height = max(max_height, books[j - 1][1])  # Update the max height on the shelf

                if width > shelfWidth:
                    break  # If the width exceeds shelfWidth, break out of the loop

                # Update dp[i] to the minimum height needed to place books 1 through i
                dp[i] = min(dp[i], dp[j - 1] + max_height)

        return dp[len(books)]
