"""Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

    The length of the segment matches Ron's birth month, and,
    The sum of the integers on the squares is equal to his birth day.

Determine how many ways she can divide the chocolate."""


def birthday(s, d, m):
    start = 0
    count = 0
    sum = 0

    for i in range(len(s)):
        sum += s[i]
        if i - start + 1 == m:
            if sum == d:
                count += 1

            sum -= s[start]
            start += 1

    return count


if __name__ == "__main__":
    print(birthday(s=[2, 2, 1, 3, 2], d=4, m=2))
