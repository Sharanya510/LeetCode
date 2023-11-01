# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
from typing import List

class Solution:
    def lower_bound(self, products: List[str], start: int, word: str) -> int:
        i, j = start, len(products)
        while i < j:
            mid = (i + j) // 2
            if products[mid] >= word:
                j = mid
            else:
                i = mid + 1
        return i

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        start, bsStart, n = 0, 0, len(products)
        prefix = ""
        for c in searchWord:
            prefix += c

            # Get the starting index of word starting with `prefix`.
            start = self.lower_bound(products, bsStart, prefix)

            # Add empty list to result.
            result.append([])

            # Add the words with the same prefix to the result.
            # Loop runs until `i` reaches the end of input or 3 times or till the
            # prefix is same for `products[i]` Whichever comes first.
            for i in range(start, min(start + 3, n)):
                if len(products[i]) < len(prefix) or not products[i].startswith(prefix):
                    break
                result[-1].append(products[i])

            # Reduce the size of elements to binary search on since we know
            bsStart = abs(start)
        return result

# Example usage
# solution = Solution()
# products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
# searchWord = "mouse"
# print(solution.suggestedProducts(products, searchWord))
