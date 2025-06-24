# LEETCODE 1004
def longestOnes(nums, k):
    n = len(nums)
    left = 0
    ans = 0
    count = {}

    for right in range(n):
        if nums[right] not in count:
            count[nums[right]] = 0
        count[nums[right]] += 1

        while 0 in count and count[0] > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans


print(longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
