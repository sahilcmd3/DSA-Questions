# Fixed Sliding window
# LEETCODE 643
# LEETCODE 1456
def maxVowels(s, k):
    vowels = {"a", "e", "i", "o", "u"}
    left = count = ans = 0

    for right in range(len(s)):
        if s[right] in vowels:
            count += 1
        if right - left + 1 > k:
            if s[left] in vowels:
                count -= 1
            left += 1
        ans = max(ans, count)
        if ans == k:  # Can't do better
            return k

    return ans


print(maxVowels(s="abciiidef", k=3))
