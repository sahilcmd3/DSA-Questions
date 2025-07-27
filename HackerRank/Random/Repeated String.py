"""There is a string,s, of lowercase English letters that is repeated infinitely many times. Given an integer, n,
find and print the number of letter a's in the first n letters of the infinite string.
"""


def repeatedString(s, n):
    count_a = s.count('a')
    full_repeats = n // len(s)
    remainder = n % len(s)
    return count_a * full_repeats + s[:remainder].count('a')


if __name__ == "__main__":
    print(repeatedString(s="a", n=1000000000000))
