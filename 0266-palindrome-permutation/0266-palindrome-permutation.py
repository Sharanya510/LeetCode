from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        my_hashmap = Counter(s)
        
        count_odd, count_even = 0, 0
        print(my_hashmap)
        for key, value in my_hashmap.items():
            if value % 2 == 1:
                count_odd += 1
            else:
                count_even += 1
        if count_odd > 1 :
            return False
        else:
            return True