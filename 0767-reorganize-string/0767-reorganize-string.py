class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        priority_queue = [(-count, char) for char, count in Counter(s).items()]
        heapify(priority_queue)
        
        while priority_queue:
            first_count, first_char = heappop(priority_queue)
            if not ans or first_char != ans[-1]:
                ans.append(first_char)
                if first_count + 1 != 0:
                    heappush(priority_queue, (first_count + 1, first_char))
            else:
                if not priority_queue: 
                    return ''
                second_count, second_char = heappop(priority_queue)
                ans.append(second_char)
                if second_count + 1 != 0:
                    heappush(priority_queue, (second_count + 1, second_char))
                heappush(priority_queue, (first_count, first_char))
                
        return ''.join(ans)
        