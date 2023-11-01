class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        shortest_distance = float("inf")
        for i in range(len(words)):
            if words[i]==word1:
                for j in range(len(words)):
                    if words[j]==word2:
                        if j>i:
                            distance=j-i
                        else:
                            distance=i-j
                        shortest_distance=min(shortest_distance,distance)
        return shortest_distance
        
#         first_index, second_index = 0, 0
#         for index, word in enumerate(wordsDict):
#             if word == word1:
#                 first_index = index
#             if word == word2:
#                 second_index = index
                
#             if second_index > first_index:
#                 distance = second_index - first_index
#             else:
#                 distance = first_index - second_index
            
#         shortest_distance = min(distance, shortest_distance)
#         return shortest_distance