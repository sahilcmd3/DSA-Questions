#LEETCODE (Hard)

"""You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all
concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of
words.

Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Approach:
Create sliding window and hash map
 - Calculating the length of word and total length: Since all words in words are of the same length, calculate the
   length of each word and the total length of the concatenated substring.
 - Hashmap: Map each word to its frequency in the words list.
 - Sliding Window: Move a sliding window of the total length of the concatenated substring across s. In each window,
   break the window into substrings of the word's length and check if these substrings form a permutation of words.
 - Track Word counts: Use the hashmap to track the counts of words in the current window. If a count of a word exceeds
   its count in the words freq map, it's not a valid window.
 - Check for Valid Concatenation: If the hashmap of the current window matches the frequency map of words, then the
   current window is a valid-concatenated substring. Add the start index of this window to the result."""


# Time Complexity: O(N×K/L+M)
def subs(s, words):
    if not words or not s:
        return []

    word_length = len(words[0])
    word_count = {}

    # Creating freq map for words
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    result = []

    # Checking for each possible window in the string
    for i in range(word_length):
        left = i
        count = 0
        temp_word_count = {}

        for j in range(i, len(s) - word_length + 1, word_length):
            word = s[j:j + word_length]
            if word in word_count:
                temp_word_count[word] = temp_word_count.get(word, 0) + 1
                count += 1

                while temp_word_count[word] > word_count[word]:
                    left_word = s[left:left + word_length]
                    temp_word_count[left_word] -= 1
                    left += word_length
                    count -= 1

                if count == len(words):
                    result.append(left)

            else:
                temp_word_count.clear()
                count = 0
                left = j + word_length

    return result


ans = subs(s="barfoothefoobarman", words=["foo", "bar"])
print(ans)
