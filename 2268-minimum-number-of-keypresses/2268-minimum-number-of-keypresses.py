class Solution:
    def minimumKeypresses(self, s: str) -> int:
        # APPROACH --> BRUTE FORCE
        # TIME COMPLEXITY --> O(N log N)
        # SPACE COMPLEXITY --> O(N)
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        # print(freq)
        freq_array = [[key, freq[key]] for key in freq.keys()]
        # print(freq_array)
        freq_array.sort(key=lambda x:x[1], reverse=True)
        # print(freq_array)
        total_press = 0
        single_press = 1
        for index, char in enumerate(freq_array):
            total_press += char[1]*single_press
            if (index+1)%9 == 0:
                single_press += 1
        return total_press
            