class Solution:
    def reorganizeString(self, s: str) -> str:
        # APPROACH --> COUNTING & PLACING ODD/EVEN
        # TIME COMPLEXITY --> O(N)
        # SPACE COMPLEXITY --> O(k)
        char_counts = Counter(s)
        max_count , letter = 0, ''
        for char, count in char_counts.items():
            if count > max_count:
                max_count = count
                letter = char
        
        # CORNER CASE --> if the max char is greater than half of the length og the input then return empty string as we cant form characters alternatively
        if max_count > (len(s) + 1)//2:
            return ''
        
        ans = [''] * len(s)
        index = 0
        
        while char_counts[letter] != 0:
            ans[index] = letter
            index += 2
            char_counts[letter] -= 1
            
        for char, count in char_counts.items():
            while count > 0:
                if index >= len(s):
                    index = 1
                ans[index] = char
                index += 2
                count -= 1
        return ''.join(ans)
        
        
        
        
        
        # APPROACH --> PRIORITY QUEUE
#         TIME COMPLEXITY --> O(N log k)
#         SPACE COMPLEXITY --> O(k)
#         ans = []
#         priority_queue = [(-count, char) for char, count in Counter(s).items()]
#         heapify(priority_queue)
        
#         while priority_queue:
#             first_count, first_char = heappop(priority_queue)
#             if not ans or first_char != ans[-1]:
#                 ans.append(first_char)
#                 if first_count + 1 != 0:
#                     heappush(priority_queue, (first_count + 1, first_char))
#             else:
#                 if not priority_queue: 
#                     return ''
#                 second_count, second_char = heappop(priority_queue)
#                 ans.append(second_char)
#                 if second_count + 1 != 0:
#                     heappush(priority_queue, (second_count + 1, second_char))
#                 heappush(priority_queue, (first_count, first_char))
#         return ''.join(ans)
        