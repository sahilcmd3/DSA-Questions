# LEETCODE 1903

"""You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a
non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string."""


def largestNum(num):
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[: i + 1]

    return ""


if __name__ == "__main__":
    print(largestNum(num="52"))
