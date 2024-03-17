class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = {}
        for i, c in enumerate(s):
            if c in index:
                index[c].append(i)
            else:
                index[c] = [i]
        # print(index)
        total_count = 0

        for c, indexes in index.items():
            for i in range(len(indexes)):
                left = indexes[i-1] if i > 0 else -1
                right = indexes[i+1] if i < len(indexes)-1 else len(s)
                left_contribution = indexes[i] - left
                right_contribution = right - indexes[i]
                total_count += left_contribution * right_contribution
                # print(left, right, left_contribution, right_contribution, total_count)
        return total_count