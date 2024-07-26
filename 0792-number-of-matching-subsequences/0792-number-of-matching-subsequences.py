class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        heads = [[] for _ in range(26)]
        
        # Initialize heads with iterators for each word
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord('a')].append(it)
        
        # print(f'Initial heads: {heads}')
        
        for letter in s:
            letter_index = ord(letter) - ord('a')
            old_bucket = heads[letter_index]
            heads[letter_index] = []
            
            # print(f'Processing letter: {letter}')
            # print(f'Old bucket before processing: {old_bucket}')
            
            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                
                # print(f'Processing iterator: {it}')
                # print(f'Next character: {nxt}')
                
                if nxt:
                    heads[ord(nxt) - ord('a')].append(it)
                else:
                    ans += 1
                    # print(f'Found a matching subsequence, updated ans: {ans}')
            
            # print(f'Heads after processing letter {letter}: {heads}')
        
        # print(f'Final result: {ans}')
        return ans

