class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_list = defaultdict(list)
        for string in strs:
            char_count = [0] * 26
            for char in string:
                char_count[ord(char) - ord('a')] += 1
            output_list[tuple(char_count)].append(string)
        return output_list.values()
    
    # ["eat","tea","tan","ate","nat","bat"]
    # output_list = []
    # count = [0]*26
    # eat --> count = [1 0 0 ]
    
    