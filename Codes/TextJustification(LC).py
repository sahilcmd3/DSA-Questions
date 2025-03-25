#LEETCODE (Hard)

"""Given an array of strings words and a width maxWidth, format the text such that each line has exactly
maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line
does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots
on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word."""


#Greedy Approach
#Time Complexity: O(n^2)
def fullJustify(words, maxWidth):
    res = []  # List to store the justified lines
    line = []  # Temporary list to hold words for the current line
    width = 0  # Tracks the total length of words in the current line

    for w in words:
        if width + len(w) + len(line) > maxWidth: # Checks if adding the current word and spaces to the line exceeds maxWidth
            # len(line) shows the space needed between the words
            for i in range(maxWidth - width): # Calculates how many spaces to be added
                line[i % (len(line) - 1 or 1)] += ' ' # Distributes spaces evenly across all gaps between words.
                # If there's only one word (len(line) - 1 = 0), spaces are added to the right of that word.
                # The % operator ensures spaces are distributed cyclically between word gaps.

            res, line, width = res + [''.join(line)], [], 0 # Joins the words in line into a single string and appends
            # it to res. Resets line and width for the next line.

        line += [w]
        width += len(w) # Adds the current word (w) to the line and updates its width

    return res + [' '.join(line).ljust(maxWidth)] # Spaces are simply added to the right using .ljust(maxWidth) to
    # make it exactly maxWidth long.
    # ljust() method is used to align strings to the left and pad them with a specified character
    # (default is a space) to meet a desired width.
    # For the last line, no extra space distribution is applied; it’s left-aligned using .ljust()


ans = fullJustify(words=["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16)
print(ans)