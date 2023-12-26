class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        first_index, second_index = -2, -2
        shortest_distance = len(words)
        for index, word in enumerate(words):
            if word == word1:
                first_index = index
            if word == word2:
                second_index = index
                
            if first_index != -2 and second_index != -2:
                # print(shortest_distance)
                shortest_distance = min(shortest_distance, abs(first_index - second_index))
        return shortest_distance
        
        
        # BRUTE -- FORCE   
        # shortest_distance = float("inf")
        # for i in range(len(words)):
        #     if words[i]==word1:
        #         for j in range(len(words)):
        #             if words[j]==word2:
        #                 if j>i:
        #                     distance=j-i
        #                 else:
        #                     distance=i-j
        #                 shortest_distance=min(shortest_distance,distance)
        # return shortest_distance
        
        