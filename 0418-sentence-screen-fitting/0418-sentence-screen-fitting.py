class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
    # Join the sentence into a single string with spaces in between and add a space at the end
        s = ' '.join(sentence) + ' '
        length = len(s)

        # Initialize the pointer and the result counter
        pointer = 0

        # Loop through each row
        for _ in range(rows):
            # Move the pointer forward by the number of columns in the row
            pointer += cols

            # If we are at a space, it means we can fit the whole row, move to the next row
            if s[pointer % length] == ' ':
                pointer += 1
            else:
                # Otherwise, move the pointer back until it points to a space
                while pointer > 0 and s[(pointer - 1) % length] != ' ':
                    pointer -= 1

    # The number of times the sentence can fit is the number of complete rotations of the pointer
        return pointer // length