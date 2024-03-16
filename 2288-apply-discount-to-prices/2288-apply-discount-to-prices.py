class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        
        for index, word in enumerate(words):
            if word.startswith('$'):
                try:
                    num = int(word[1:])
                    discounted_price = num * (1 - discount / 100)
                    words[index] = f'${discounted_price:.2f}'
                except ValueError:
                    # If the word after '$' cannot be converted to an integer, skip it
                    pass
                
        return ' '.join(words)

