class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False

        # Remove all 'X' and compare the remaining strings
        if start.replace('X', '') != end.replace('X', ''):
            return False

        # Check the position constraints for 'L' and 'R'
        j = 0
        for i in range(len(start)):
            if start[i] == 'L':
                # Move j to the next 'L' in end
                while end[j] != 'L':
                    j += 1
                # 'L' can only move to the left, so start[i] should be to the right of end[j]
                if i < j:
                    return False
                j += 1

        j = 0
        for i in range(len(start)):
            if start[i] == 'R':
                # Move j to the next 'R' in end
                while end[j] != 'R':
                    j += 1
                # 'R' can only move to the right, so start[i] should be to the left of end[j]
                if i > j:
                    return False
                j += 1

        return True
    
    
# R   X   X   L   R   X   R   X   L
# R           L   R       R       L

# X   R   L   X   X   R   R   L   X
#     R   L           R   R   L