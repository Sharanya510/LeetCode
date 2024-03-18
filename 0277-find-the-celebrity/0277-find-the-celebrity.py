# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # APPROACH --> BRUTE FORCE
        numberofpeople = n
        for i in range(n):
            if self.isCelebrity(i, numberofpeople):
                return i
        return -1
    
    def isCelebrity(self, i, numberofpeople):
        for j in range(numberofpeople):
            if i == j:
                continue
            if knows(i , j ) or not knows(j, i) :
                return False
        return True