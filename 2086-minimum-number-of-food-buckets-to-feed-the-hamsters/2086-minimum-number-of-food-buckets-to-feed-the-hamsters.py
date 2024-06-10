class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        # When we see a hamster
        # ASK:
        # Was it fed on the left :
        # If yes, move on
        # if no, try to feed it on the right, than the left
        # if we cannot, return -1
        # Why should we feed a hamster on the right first?
        # Because the food can be reused to feed another hamster
        count = 0
        hamsters = list(hamsters)
        for i in range(len(hamsters)):
            if hamsters[i] != 'H': continue
            if i - 1 >= 0 and hamsters[i - 1] == 'B':  # 'B' = bucket
                continue
            if i + 1 <= len(hamsters) - 1 and hamsters[i + 1] == '.':
                # can be fed on the right
                hamsters[i + 1] = 'B'
                count += 1
            elif i - 1 >= 0 and hamsters[i - 1] == '.':
                count += 1
            else:
                return -1

        return count